import json
from django.shortcuts import render
from .models import CustomUser, Fund
from fund.forms import RegistrationForm
from .forms import FundForm
import hashlib
from .models import Fund
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'fund/home.html')

def fund(request):
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')  # Redirect to home page after successful form submission
    else:
        form = FundForm()
    return render(request,'fund/fund.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new CustomUser object with form data
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Optionally, you can log in the user after registration
            # login(request, user)
            return redirect('home')  # Redirect to the homepage after registration
    else:
        form = RegistrationForm()
    return render(request, 'fund/registration.html', {'form': form})

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Renamed login function
            return redirect('home')  # Redirect to the homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'fund/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')


# views.py
from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.urls import reverse

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))
    else:
        form = TransactionForm()
    return render(request, 'fund/transaction_form.html', {'form': form})


def success_view(request):
    return render(request, 'fund/success.html')

import hashlib
from django.contrib.auth.decorators import login_required

@login_required
def transaction(request):
    current_user = request.user.username
    funds = Fund.objects.all()
    hashed_funds = []
    for fund in funds:
        if fund.name == current_user:
            hashed_fund = {
                'name': fund.name,
                'amount': fund.amount,
                'mobile': fund.mobile,
                'email': fund.email,
                'description': fund.description
            }
        else:
            hashed_fund = {
                'name': hashlib.sha256(fund.name.encode()).hexdigest(),
                'amount': hashlib.sha256(str(fund.amount).encode()).hexdigest(),
                'mobile': hashlib.sha256(fund.mobile.encode()).hexdigest(),
                'email': hashlib.sha256(fund.email.encode()).hexdigest(),
                'description': hashlib.sha256(fund.description.encode()).hexdigest()
            }
        hashed_funds.append(hashed_fund)
    return render(request, 'fund/transactions.html', {'funds': hashed_funds})
