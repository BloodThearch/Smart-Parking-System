import re
from django.shortcuts import render
from login.models import Account
# Create your views here.

def home(request):
    return render(request, 'home.html');

def services(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        try:
            acc = Account.objects.get(mobile_number=mNum)
        except:
            return render(request, 'unregisteredNumber.html')
        else:
            return render(request, 'services.html', {"acc": acc})