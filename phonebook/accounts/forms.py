from django.db import models
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput)


class UserRegisterFrom(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=50, required=True, widget=forms.EmailInput)
    password = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("your email has already exist")
        else:
            return email
