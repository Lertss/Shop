from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import admin
from .models import User


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


