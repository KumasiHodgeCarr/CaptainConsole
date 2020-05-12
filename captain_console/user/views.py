from django.contrib import messages
from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileForm, CustomUserCreationForm
from user.models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/register.html', {'form': form})


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('profile')

    return render(request,'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })