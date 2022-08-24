from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request , "hello/index.html")


def brien(request) :
    return HttpResponse("Hello BOOOO")

def greeting(request , name ) :
    # return HttpResponse(f"Helloo {name.capitalize()}")
    return render(request , "hello/greet.html" , {
        "name" : name.capitalize()
    })

