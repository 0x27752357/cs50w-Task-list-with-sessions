from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form) :
    task = forms.CharField(label="Add Task ")
    # priority = forms.IntegerField(label="Priority" , min_value=1 , max_value=10)

# Create your views here.
Tasks = []

def index(request) :
    return render(request , "tasks/index.html",{
        "tasks" : Tasks
    })

def add(request) : 
    if request.method == "POST" :
        form = NewTaskForm(request.POST)
        if form.is_valid() : 
            task = form.cleaned_data["task"]
            Tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
        else : 
            return render(request , "tasks/add.html" , {
                "form" : form 
            })
    
    return render(request , "tasks/add.html" ,{
        "form" : NewTaskForm()
    })