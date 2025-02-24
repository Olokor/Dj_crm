from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm
# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "first_name":"wisdom", "age":78, "class":"java class", "leads":leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, "leads/lead_detail.html", {"lead":lead})

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            agent = Agent.objects.first()
            Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
            return redirect("leads:home")

    context = {
        "form":form
    }
    return render(request, "leads/lead_form.html", context)