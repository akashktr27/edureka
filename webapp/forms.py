from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Login_users

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

class Login_forms(UserCreationForm):
    class Meta:
        model   = Login_users
        fields  = '__all__'
