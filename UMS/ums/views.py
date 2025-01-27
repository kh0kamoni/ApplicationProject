from django.shortcuts import render
import datetime

# Create your views here.
def landing(request):
    date = datetime.datetime.now()
    return render(request, "ums/landing.html", {
        "year": date.year
    })

def signup(request):
    return render(request, "ums/signup.html")
