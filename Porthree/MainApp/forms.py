"""
This module contains all forms for data posting
"""
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserDetails
from .models import Skill, Project

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['email', 'first_name', 'last_name', 'career_title', 'phone_number', 'about_me', 'resume']
        fields.append("profile_picture")
        widgets = {
            'resume': forms.FileInput(attrs={'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'about', 'comment', 'rating']

class SignUpForm(UserCreationForm):
    # Add custom fields if needed
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass
