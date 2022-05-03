from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from login.models import Account
from checkin.models import ParkedVehicles
from checkout.models import LeftVehicles

# Create your views here.

def checkout(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        try:
            acc = Account.objects.get(mobile_number=mNum)
            pv = ParkedVehicles.objects.get(mobile_number=acc)
        except:
            return render(request, 'notcheckedin.html', {"acc": acc})
        else:
            return render(request, 'checkout.html', {"acc": acc})

def checkoutComp(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        try:
            acc = Account.objects.get(mobile_number=mNum)
            pv = ParkedVehicles.objects.get(mobile_number=acc)
        except:
            return render(request, 'notcheckedin.html', {"acc": acc})
        else:
            try:
                lf = LeftVehicles()
                # to be continued
            except:
                return render(request, 'checkin.html', {"acc": acc})
            else:
                return render(request, 'checkinComp.html', {"acc": acc})

