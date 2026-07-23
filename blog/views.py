from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Post

def index(request):
    return render(request, 'blog/home_page.html')

def choice(request, post_slug):

    post = get_object_or_404(
        Post,
        slug = post_slug,
        is_published = 1,
    )

    return render(request, 'blog/post_page.html', {
        'title' : post.title,
        'content': post.content,
    })