from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

# Create your models here.

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=50, 
        required=True, 
        help_text="Enter Username",
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Username',
            }),)

    password1 = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Password'
            }),)

    password2 = forms.CharField(
        required = True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Password Again'
            }),)
    
    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2', 'check',
        ]