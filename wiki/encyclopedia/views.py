from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def css(request):
    markdowner = Markdown()
    csspage = util.get_entry("CSS")
    #markdowner.convert(fileReader.read)
    #return render(request, "encyclopedia/index.html", {
    #    "entries": util.list_entries()
    #})
    return HttpResponse(markdowner.convert(csspage))

