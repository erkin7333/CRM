from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def add_lead(request):
    """............"""
    return render(request, 'crm_core/add-lead.html')