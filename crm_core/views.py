from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddLeadForm, AddCommentForm, AddFileForm
from .models import Lead
from client.models import Client, Comment as ClientComment
from team.models import Team
from django.views.generic import ListView, UpdateView, CreateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


class LeadListView(LoginRequiredMixin, ListView):
    """Foydalanuvchilarni bazadan malumotlarin olish Class based views"""
    model = Lead
    template_name = 'crm_core/lead-list.html'

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user, converted_to_client=False)
        return queryset


@login_required
def lead_list(request):
    """Foydalanuvchilarni bazadan malumotlarin olish funksiyasi"""

    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
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
    return render(request, 'crm_core/lead_detail.html', context=context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    """Foydalanuvchini batafsil malumotlarini ko'rish uchun Class based views"""
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm
        context['file_forms'] = AddFileForm()
        return context
    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, id=self.kwargs.get('pk'))



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


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    """Foydalanuvchini yangilash uchun Class based views"""
    model = Lead
    template_name = 'crm_core/lead-edit.html'
    fields = ('name', 'email', 'description', 'priority', 'status')
    success_url = reverse_lazy('crm_core:leads')



@login_required
def add_lead(request):
    """Foydalanuvchi qo'shish uchun funksiya"""

    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()
            messages.success(request, "Foydalanuvchi qo'shildi")
            return redirect('crm_core:leads')
    else:
        form = AddLeadForm()
    return render(request, 'crm_core/add-lead.html', {'form': form, 'team': team})


class LeadCreateView(LoginRequiredMixin, CreateView):
    """Foydalanuvchi qo'shish uchun Class based views"""
    model = Lead
    template_name = 'crm_core/add-lead.html'
    fields = ('name', 'email', 'description', 'priority', 'status')
    success_url = reverse_lazy('crm_core:leads')

    def form_valid(self, form):
        team = Team.objects.filter(created_by=self.request.user)[0]
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()
        return



@login_required
def convert_to_client(request, pk):
    """Yetakchi Foydalanuvchini Mijozga aylantirish funksiyasi"""

    lead = get_object_or_404(Lead, created_by=request.user, id=pk)[0]
    team = Team.objects.filter(created_by=request.user)[0]
    client = Client.objects.create(
        name=lead.name, email=lead.email,
        created_by=request.user,
        description=lead.description,
        team=team
    )
    lead.converted_to_client = True
    lead.save()

    comments = lead.comments.all()
    for comment in comments:
        ClientComment.objects.create(
            client=client,
            content=comment.content,
            created_by=comment.created_by
        )

    messages.success(request, "Foydalanuvchi Mijozga aylantirildi")
    return redirect('crm_core:leads')


class AddCommentView(View):
    """Cometariya qoldirish uchun Class based views"""

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        content = request.POST.get('content')
        form = AddCommentForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()
        print("AAAAAAAAAAAA=========", content)
        print("WWWWWWWWWWw======", pk)

        return redirect('crm_core:lead_detail', pk=pk)


class AddFileView(View):
    """Fayil yuklash uchun Class based views"""

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            file = form.save(commit=False)
            file.team = team
            file.lead_id = pk
            file.created_by = request.user
            file.save()
        return redirect('crm_core:lead_detail', pk=pk)
