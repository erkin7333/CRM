from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
from django.contrib import messages
from team.models import Team



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

    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()
            messages.success(request, "Client qo'shildi")
            return redirect('client:client')
    else:
        form = ClientForm()
        context = {
            'form': form,
            'team': team
        }
    return render(request, 'client/client-add.html', context=context)


@login_required
def edit_client(request, pk):
    """Client malumotlarini yangilash uchun funksiya"""

    client = get_object_or_404(Client, created_by=request.user, id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client malumotlari o'zgartirildi!")
            return redirect('client:client')
    else:
        form = ClientForm(instance=client)
        context = {'form': form}
    return render(request, 'client/edit-client.html', context=context)


@login_required
def client_delete(request, pk):
    """Clientni o'chirish funksiyasi..."""

    client = get_object_or_404(Client, created_by=request.user, id=pk)
    client.delete()
    messages.success(request, "Client o'chirildi")
    return redirect('client:client')