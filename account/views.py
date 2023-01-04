from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from django.contrib.auth.decorators import login_required
from team.models import Team


def signup(request):
    """Ro'yxatdan o'tish uchun funksiya"""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            team = Team.objects.create(name='Jamoa nomi', created_by=request.user)
            team.members.add(request.user)
            team.save()
            return redirect("account:login")
    else:
        form = UserCreationForm()
    return render(request, 'account/sign-up.html', {'form': form})


def user_login(request):
    """Aftorizatsiyadan o'tish uchun funksiya"""

    return render(request, 'account/login.html')


@login_required
def myaccount(request):
    """My Account uchun funksiya"""

    teams = Team.objects.filter(created_by=request.user)[0]
    context = {
        'teams': teams
    }
    return render(request, 'account/myaccount.html', context=context)
