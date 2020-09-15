from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from encyclopedia import util

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(widget=forms.Textarea(attrs={"style": "height:400px; resize: none;"}))


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if util.get_entry(title) == None:
                entry = form.cleaned_data["entry"]
                #write entry to md file
                return HttpResponse("Success:" + title + "<br>" + "<a href=" + "/" + ">Home</a>")
            else:
                return HttpResponse("Error:" + title + " already exists<br>" + "<a href=" + "/" + ">Home</a>")
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "newpage/index.html", {
            "form": NewTaskForm()
        })
