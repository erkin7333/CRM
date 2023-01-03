from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddLeadForm
from .models import Lead
from client.models import Client


@login_required
def lead_list(request):
    """Foydalanuvchilarni bazadan malumotlarin olish funksiyasi"""

    leads = Lead.objects.filter(created_by=request.user)
    context = {
        'leads': leads
    }
    return render(request, 'crm_core/lead-list.html', context=context)


@login_required
def lead_deteil(request, pk):
    """Foydalanuvchini batafsil malumotlarini ko'rish uchun funksiya"""

    lead_d = get_object_or_404(Lead, created_by=request.user, id=pk)
    context = {
        'lead_d': lead_d
    }
    return render(request, 'crm_core/lead-deteil.html', context=context)


@login_required
def lead_delete(request, pk):
    """Foydalanuvchini o'chirish uchun funksiya"""

    lead = get_object_or_404(Lead, created_by=request.user, id=pk)
    lead.delete()
    messages.success(request, "Malumot o'chirildi")
    return redirect('crm_core:leads')


@login_required
def edit_lead(request, pk):
    """Foydalanuvchini yangilash uchun funksiya"""

    lead = get_object_or_404(Lead, created_by=request.user, id=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Foydalanuvchi malumotlari o'zgartirildi!")
            return redirect('crm_core:leads')
    else:
        form = AddLeadForm(instance=lead)
        context = {'form': form}
    return render(request, 'crm_core/lead-edit.html', context=context)

@login_required
def add_lead(request):
    """Foydalanuvchi qo'shish uchun funksiya"""

    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, "Foydalanuvchi qo'shildi")
            return redirect('crm_core:leads')
    else:
        form = AddLeadForm()
    return render(request, 'crm_core/add-lead.html', {'form': form})


@login_required
def convert_to_client(request, pk):
    """Yetakchi Foydalanuvchini Mijozga aylantirish funksiyasi"""

    lead = get_object_or_404(Lead, created_by=request.user, id=pk)
    client = Client.objects.create(
        name=lead.name, email=lead.email,
        created_by=request.user,
        description=lead.description
    )
    lead.converted_to_client = True
    lead.save()
    messages.success(request, "Foydalanuvchi Mijozga aylantirildi")
    return redirect('crm_core:leads')