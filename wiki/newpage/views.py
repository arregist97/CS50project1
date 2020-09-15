from django import forms
from django.shortcuts import render
from django.http import HttpResponse
class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(widget=forms.Textarea(attrs={"style": "height:400px; resize: none;"}))


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]
#            return HttpResponseRedirect(reverse("tasks:index"))
            return HttpResponse("Success:" + title + "<br>" + "<a href=" + "/" + ">Home</a>")
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "newpage/index.html", {
            "form": NewTaskForm()
        })
