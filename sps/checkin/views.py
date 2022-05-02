from django.shortcuts import render
from django.utils import timezone
from login.models import Account
from checkin.models import ParkedVehicles

# Create your views here.

def checkin(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        try:
            acc = Account.objects.get(mobile_number=mNum)
        except:
            return render(request, 'unregisteredNumber.html')
        else:
            return render(request, 'checkin.html', {"acc": acc})

def checkinComp(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        try:
            acc = Account.objects.get(mobile_number=mNum)
        except:
            return render(request, 'unregisteredNumber.html')
        else:
            try:
                pv = ParkedVehicles()
                pv.mobile_number = acc
                pv.save()
            except:
                return render(request, 'checkin.html', {"acc": acc})
            else:
                return render(request, 'checkinComp.html', {"acc": acc})