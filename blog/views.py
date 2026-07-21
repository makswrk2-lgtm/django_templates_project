from django.http import Http404
from django.shortcuts import render
from django.template.defaultfilters import slugify
from .data import menu_db


def index(request):
    return render(request, 'blog/home_page.html')


def choice(request, slug):
    for i in menu_db:
        if slugify(i['title']) == slug:
            return render(request, 'blog/post_page.html', {'post': i})
    raise Http404("Post not found")