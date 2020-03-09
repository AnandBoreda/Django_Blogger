from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def single(request):
    return render(request, 'single.html')

def lifestyle(request):
    return render(request, 'lifestyle.html')

def health(request):
    return render(request, 'health.html')

def family(request):
    return render(request, 'family.html')

def technology(request):
    return render(request, 'technology.html')

def travel(request):
    return render(request, 'travel.html')

def work(request):
    return render(request, 'work.html')

