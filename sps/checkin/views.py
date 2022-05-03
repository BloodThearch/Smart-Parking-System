from django.shortcuts import render
from django.utils import timezone
from login.models import Account
from checkin.models import ParkedVehicles, Slot

# Create your views here.

def checkin(request):
    if request.method == 'POST':
        mNum = request.POST['mobile_number']
        slot = Slot.objects.all()[0]
        if slot.available_slots > 0:
            try:
                acc = Account.objects.get(mobile_number=mNum)
            except:
                return render(request, 'unregisteredNumber.html')
            else:
                return render(request, 'checkin.html', {"acc": acc})
        else:
            return render(request, 'slotsfull.html', {"acc": acc})

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
                slot = Slot.objects.all()[0]
                slot.available_slots = slot.available_slots - 1
                slot.save()
                slot = Slot.objects.all()[1]
                slot.delete()
            except:
                return render(request, 'checkin.html', {"acc": acc})
            else:
                return render(request, 'checkinComp.html', {"acc": acc})