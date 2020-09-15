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
        "text": body
    })

