from pickle import NONE
from django.shortcuts import render
from login.models import Account
from .forms import SignUpForm

# Create your views here.

def signupPage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'signupComp.html', {})
    else:
        return render(request, 'signup.html', {})