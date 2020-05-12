from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileUpdateForm, UserUpdateForm
from user.models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account{username} has been created! You are now able to log in ')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileUpdateForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('profile')

    return render(request,'user/profile.html', {
        'form': ProfileUpdateForm(instance=profile)
    })


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct error before')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })


