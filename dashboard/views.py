from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    """Dashboard panel uchun funksiya"""
    return render(request, 'dashboard/dashboard.html')