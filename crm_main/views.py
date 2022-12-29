from django.shortcuts import render



def homepage(request):
    """Home page uchun funksiya"""
    return render(request, 'crm_main/home.html')


def aboutpage(request):
    """About page uchun funksiya"""
    return render(request, 'crm_main/about.html')
