from django.shortcuts import render, get_object_or_404
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm




@login_required
def client_list(request):
    """Bazadan Klienlar ro'ycatinii olish funksiyasi"""

    clients = Client.objects.filter(created_by=request.user)
    context = {
        'clients': clients
    }
    return render(request, 'client/client-list.html', context=context)


@login_required
def client_detail(request, pk):
    """Klientni batafsil malumotlarini ko'rish funksiyasi"""

    client = get_object_or_404(Client, created_by=request.user, id=pk)
    context = {
        'client': client
    }
    return render(request, 'client/client-detail.html', context=context)


@login_required
def client_add(request):
    """Client qo'shish uchun funksiy"""

    pass