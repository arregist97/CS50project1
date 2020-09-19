from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse

#python manage.py runserver
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def css(request):
    markdowner = Markdown()
    csspage = util.get_entry("CSS")
    body = markdowner.convert(csspage)
    #markdowner.convert(fileReader.read)
    #return render(request, "encyclopedia/index.html", {
    #    "entries": util.list_entries()
    #})
    #return HttpResponse('{% extends "encyclopedia/layout.html" %}{% block title %}' + body + '{% endblock %}')
#    return render(request, "encyclopedia/entry.html", {
#        "text": "hi"
#    })'''
    return render(request, "encyclopedia/entry.html", {
        "text": body, 
        "title":"CSS"
    })
def page(request, entry):
    markdowner = Markdown()
    mdpage = util.get_entry(entry)
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
        elif(len(matches) == 1):
            markdowner = Markdown()
            mdpage = util.get_entry(matches[0])
            body = markdowner.convert(mdpage)
            return render(request, "encyclopedia/entry.html", {
                "text": body, 
                "title": matches[0]
        })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": matches
            })

