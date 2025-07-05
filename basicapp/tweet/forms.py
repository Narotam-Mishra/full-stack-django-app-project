from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# user-defined form
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

# buit-in form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
