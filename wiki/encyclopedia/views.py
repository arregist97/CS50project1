from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from random import randrange

#python manage.py runserver
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "title": "All Pages",
        "entries": util.list_entries()
    })
def page(request, entry):
    markdowner = Markdown()
    mdpage = util.get_entry(entry)
    if (mdpage == None):
        return HttpResponse("No matches found for " + entry + ".<br>" + "<a href=" + "/" + ">Home</a>")
    body = markdowner.convert(mdpage)
    return render(request, "encyclopedia/entry.html", {
        "text": body, 
        "title": entry
    })
def search(request):
    if request.method == "POST":
        ibcm = request.POST
        query = ibcm['query']
        #make everything lowercase for comparisons
        entries = util.list_entries()
        #find all matches
        matches = []
        for entry in entries:
            if not((entry.lower()).find(query.lower()) == -1):
                matches.append(entry)
        #render matches
        if(len(matches) == 0):
            return HttpResponse("No matches found for " + query + ".<br>" + "<a href=" + "/" + ">Home</a>")
        elif(matches[0].lower() == query.lower()):
            markdowner = Markdown()
            mdpage = util.get_entry(matches[0])
            body = markdowner.convert(mdpage)
            return redirect("/wiki/" + matches[0])
        else:
            return render(request, "encyclopedia/index.html", {
                "title": "Results for '" + query + "'",
                "entries": matches
            })
def randompage(request):
    entries = util.list_entries()
    randomVal= randrange(len(entries))
    return redirect("/wiki/" + entries[randomVal])


