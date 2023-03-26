from django.shortcuts import render
import markdown
from django.shortcuts import HttpResponseRedirect

from . import util


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    html_content = md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This page does not exist"
        })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "title": title,
            "content": html_content
        })
    
def search(request):
    value = request.GET.get('q','')
    if md_to_html(value) is not None:
        return HttpResponseRedirect('/wiki/' + value)
    else:
        SubStrEntry = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                return render(request, "encyclopedia/search.html", {
                    "entries": SubStrEntry,
                    "search": True,
                    "value":value
                })