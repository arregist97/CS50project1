from django import forms
from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from encyclopedia import util

class EditPageForm(forms.Form):
    entry = forms.CharField(widget=forms.Textarea(attrs={"style": "height:400px; resize: none;"}))

def editpage(request, entry):
    title = entry
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"]
            #write entry to md file
            util.save_entry(title, entry)
            return HttpResponseRedirect("/wiki/"+title)
    else:
        content = util.get_entry(title)
        tempform = EditPageForm(initial={'entry':content})
        return render(request, "encyclopedia/editpage.html", {
            "form": tempform,
            "title": title,
            "urlpost": "/editpage/"+title
        })


