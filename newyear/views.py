from django.shortcuts import render
import datetime
# Create your views here.

def index(request) :
    now = datetime.datetime.now()
    print(now.day == 22)
    return render(request , "newyear/index.html" , {
        "newyear": (now.month == 8 and now.day == 21)
    })
    
