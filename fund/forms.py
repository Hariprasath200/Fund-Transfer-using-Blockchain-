# forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

   

# forms.py
from django import forms
from .models import Fund

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ['name', 'amount', 'mobile', 'email','description']

# forms.py
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'recipient', 'amount']
