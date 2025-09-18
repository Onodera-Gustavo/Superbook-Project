from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Hero
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import HeroForm



def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

def lista_herois(request):
    herois = Hero.objects.all()  
    return render(request, "heroes/lista_herois.html", {"herois": herois})

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"  

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_herois')
    else:
        form = HeroForm()

    return render(request, "heroes/form_heroi.html", {"form": form})
