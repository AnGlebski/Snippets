from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = get_base_context(request, 'Добавление нового сниппета')
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.all()
    context["snippets"] = snippets
    # print("context = ", context)
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, snippet_id):
    pass