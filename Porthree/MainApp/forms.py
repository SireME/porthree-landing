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
        fields = ['email', 'first_name', 'last_name', 'career_title', 'phone_number', 'about_me', 'resume']
        fields.append("profile_picture")
        widgets = {
            'resume': forms.FileInput(attrs={'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
        }

class SignUpForm(UserCreationForm):
    # Add custom fields if needed
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Enter your First name"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Enter your First name"}
            ),
        }


class LoginForm(AuthenticationForm):
    pass
