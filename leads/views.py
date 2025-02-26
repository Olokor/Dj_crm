from django.urls import reverse
from lib2to3.fixes.fix_input import context
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm
# Create your views here.

class LandingPage(generic.TemplateView):
    template_name = 'landing_page.html'

class Lead_List(generic.ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    queryset = Lead.objects.all()

class Lead_Detail(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'
    queryset = Lead.objects.all()

class Lead_Create(generic.CreateView):
    template_name = 'leads/lead_form.html'
    context_object_name = 'lead'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:home")

class Lead_update(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:home")
def landing_page(request):
    return render(request, 'landing_page.html')
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "first_name":"wisdom", "age":78, "class":"java class", "leads":leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, "leads/lead_detail.html", {"lead":lead})

# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":lead_update.html
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
#             return redirect("leads:home")
#
#     context = {
#         "form":form
#     }
#     return render(request, "leads/lead_form.html", context)

# alternative method for create lead with django model form
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leads:home")

    context = {
        "form":form
    }
    return render(request, "leads/lead_form.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("leads:home")
    context = {
        "form":form,
        "lead":lead
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("leads:home")
