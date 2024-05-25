from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def worker(request):
    return render(request, 'worker.html')

def technology(request):
    return render(request, 'technology.html')
