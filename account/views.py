from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile


def signup(request):
    """Ro'yxatdan o'tish uchun funksiya"""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            return redirect("account:login")
    else:
        form = UserCreationForm()
    return render(request, 'account/sign-up.html', {'form': form})


def user_login(request):
    """Aftorizatsiyadan o'tish uchun funksiya"""

    return render(request, 'account/login.html')
