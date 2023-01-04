from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from crm_core.models import Lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    """Dashboard panel uchun funksiya"""

    team = Team.objects.filter(created_by=request.user)[0]
    leads = Lead.objects.filter(team=team).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]
    context = {
        'leads': leads,
        'clients': clients
    }
    return render(request, 'dashboard/dashboard.html', context=context)