import re
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html');

def services(request):
    return render(request, 'services.html');