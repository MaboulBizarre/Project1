from django.shortcuts import render
import markdown

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
    if request.method == "POST":
        entry_search = request
        html_content = md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/wiki.html", {
                "title": entry_search,
                "content": html_content
            })