from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class BoardingHouseForm(ModelForm):
    class Meta:
        model = BoardingHouse
        fields = '__all__'
        exclude = ['owner']
