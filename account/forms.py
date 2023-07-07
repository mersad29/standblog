# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # username = UserCreationForm.fields()
        # email = UserCreationForm.fields()
        # password1 = UserCreationForm.fields()
        # password2 = UserCreationForm.fields()
        fields = ['username', 'email', 'password1', 'password2']
