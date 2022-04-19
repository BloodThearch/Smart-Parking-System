from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "ownerName": "Gautam",
    } # This is basically python dictionary
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")