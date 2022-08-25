from django.shortcuts import render

# Create your views here.
Tasks = ["one" , "two" , "three"]

def index(request) :
    return render(request , "tasks/index.html",{
        "tasks" : Tasks
    })

def add(request) : 
    return render(request , "tasks/add.html" ,{
        
    })