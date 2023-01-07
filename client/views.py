from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm, AddCommentForm, AddFileForm
from django.contrib import messages
from team.models import Team
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import csv
from django.http import HttpResponse


class ClientListView(LoginRequiredMixin, ListView):
    """Bazadan Klienlar ro'ycatinii olish Class based views"""

    model = Client
    template_name = 'client/client-list.html'

    def get_queryset(self):
        queryset = super(ClientListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user)

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

    team = Team.objects.filter(created_by=request.user)[0]
    client = get_object_or_404(Client, created_by=request.user, id=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.client = client
            comment.save()
            return redirect('client:client_detail', id=pk)
    else:
        form = AddCommentForm()
    context = {
        'client': client,
        'form': form,
        'file_form': AddFileForm()
    }
    return render(request, 'client/client-detail.html', context=context)


@login_required
def client_add_file(request, pk):
    """Fayil yuklash uchun fubksiya"""

    team = Team.objects.filter(created_by=request.user)[0]
    client = get_object_or_404(Client, created_by=request.user, id=pk)
    if request.method == "POST":
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.team = team
            file.client_id = pk
            file.created_by = request.user
            file.save()
            return redirect('client:client_detail', pk=pk)

@login_required
def client_export(request):
    """Faylinii yuklab olish uchun funksiya"""

    clients = Client.objects.filter(created_by=request.user)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="client.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Client', 'Description', 'Created at', 'Created by'])

    for client in clients:
        writer.writerow([client.name, client.description, client.created_at, client.created_by])
    return response



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