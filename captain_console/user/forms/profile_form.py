from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm,widgets
from user.models import Profile

from django.contrib.auth.forms import UserCreationForm





class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_image']

