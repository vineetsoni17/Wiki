from django.shortcuts import render
from django import forms
from django.http import HttpResponse

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "All Pages"
    })

def title(request, name):
    return render(request, "encyclopedia/title.html", {
        "name": name,
        "body": util.get_entry(name)
    })

def query(request):
    awww=util.list_entries()
    search=(request.GET).clean_data["searchs"]
    entries=[]
    for str in awww:
        if str.find(search)==-1:
            break
        else:
            entries.append(str)
    return render(request, "encyclopedia/index.html",{
        "entries": entries,
        "title": f"Search Result: {search}"
    })


    
    