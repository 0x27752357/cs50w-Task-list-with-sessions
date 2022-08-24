from re import L
from django.shortcuts import render

# Create your views here.
Tasks = ["one" , "two" , "three"]

def index(request) :
    return render(request , "tasks/index.html",{
        "tasks" : Tasks
    })