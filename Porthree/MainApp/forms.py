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
        fields = [
            "email",
            "first_name",
            "last_name",
            "career_title",
            "phone_number",
            "rating",
            "about_me",
            "resume",
        ]
        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your First name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your Last Name"}
            ),  # Corrected
            "career_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your Career Title",
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your Phone number",
                }
            ),
            "about_me": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "About user here..."}
            ),
            "rating": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Rating"}
            ),
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
