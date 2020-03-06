from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def login(request):
    return render(request, 'login.html')

def services(request):
    return render(request, 'services.html')

def single(request):
    return render(request, 'single.html')
    
def registration(request):
    return render(request, 'registration.html')

