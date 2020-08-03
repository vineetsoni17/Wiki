from django.shortcuts import render
from django import forms
from django.http import HttpResponse

from . import util

class SearchQuery(forms.Form):
    q=forms.CharField(help_text="Search Encyclopedia")

def index(request):
    if request.method== "POST":
        query=request.POST.get("q")
        entries=[]
        aww=util.list_entries
        for stri in aww:
            if (stri.lowercase()).find(query.lowercase())!=-1:
                entries.append(stri)
        return render(request, "encyclopedia/index.html", {
            "entries": entries,
            "title": f"Search Result: {query.capitalize()}",
            "form": SearchQuery(request.POST)
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "title": "All Pages",
            "form": SearchQuery()
    })

def title(request, name):
    return render(request, "encyclopedia/title.html", {
        "name": name,
        "body": util.get_entry(name),
        "form": SearchQuery()
    })


    
    