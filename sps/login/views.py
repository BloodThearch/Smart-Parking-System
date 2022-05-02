from django.shortcuts import render
from login.models import Account
# from .forms import LogInForm

# Create your views here.

def loginPage(request):
    if request.method == "POST":
        mNum = request.POST['mobile_number']
        passwd = request.POST['pwd']
        try:
            acc = Account.objects.get(mobile_number=mNum)
        except:
            return render(request, 'unregisteredNumber.html')
        else:
            if (acc.pwd == passwd):
                return render(request, 'services.html')
            else:
                return render(request, 'wrongpwd.html')
    else:
        return render(request, 'login.html', {})

def wrongpwd(request):
    return render(request, 'wrongpwd.html')

def unregisteredNumber(request):
    return render(request, 'unregisteredNumber.html')