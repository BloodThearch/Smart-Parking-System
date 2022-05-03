from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from login.models import Account
from checkin.models import ParkedVehicles, Slot
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
                lf.mobile_number = acc;
                lf.time_in = pv.time_in
                lf.time_out = timezone.now()
                duration = (lf.time_out - lf.time_in).total_seconds()/3600
                rate = 10
                lf.bill = rate * duration
                lf.transaction_id = str(timezone.now().year)+str(timezone.now().month)+str(timezone.now().day)+str(timezone.now().hour)+str(timezone.now().minute)+str(timezone.now().second)
                lf.save()
                slot = Slot.objects.all()[0]
                slot.available_slots = slot.available_slots + 1
                slot.save()
                slot = Slot.objects.all()[0]
                slot.delete()
            except:
                return render(request, 'checkout.html', {"acc": acc})
            else:
                pv.delete()
                return render(request, 'checkoutComp.html', {"acc": acc})

