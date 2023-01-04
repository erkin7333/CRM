from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team
from .forms import TeamForm


@login_required
def edit_team(request, pk):
    """Jamoa malumotini o'zgartirish funksiyasi"""

    team = get_object_or_404(Team, created_by=request.user, id=pk)
    form = TeamForm(request.POST, instance=team)  # define the form variable here
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('account:myaccount')
    else:
        form = TeamForm(instance=team)
    return render(request, 'team/edit-team.html', {
        'form': form,
        'team': team,
    })
