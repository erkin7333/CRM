from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team


@login_required
def edit_team(request, pk):
    """Jamoa malumotini o'zgartirish funksiyasi"""

    team = get_object_or_404(Team, created_by=request.user, id=pk)
    context = {
        'team': team
    }
    return render(request, 'team/edit-team.html', context=context)

