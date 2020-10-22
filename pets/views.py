from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import *
from .forms import *
from django.urls import reverse


def home(request):
   return render(request, 'pethome/home.html',
                 {'pethome': home})

def about_us(request):
    return render(request, 'pethome/about_us.html',
                  {'about_us': about_us})

def donate(request):
    return render(request, 'pethome/donate.html',
                  {'donate': donate})

def cats(request):
    cats = Cat.objects.all()
    return render(request, 'pethome/cats_landing_page.html',
                  {'cats': cats})

def dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'pethome/dogs_landing_page.html',
                 {'dogs': dogs})

def dog_view(request, name):
    dogs = Dog.objects.all()
    dog_view = get_object_or_404(Dog, name=name)
    return render(request, 'profile')