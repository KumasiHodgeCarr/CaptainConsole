from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from user.models import Profile




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_image']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']

