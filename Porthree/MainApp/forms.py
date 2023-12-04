"""
This module contains all forms for data posting
"""
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserDetails


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['email', 'first_name', 'last_name', 'career_title', 'phone_number', 'rating', 'about_me', 'resume']

class SignUpForm(UserCreationForm):
    # Add custom fields if needed
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass
