from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('fund',views.fund,name='fund'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('success/', views.success_view, name='success'),
    path('transactions', views.transaction, name='transaction'),


]