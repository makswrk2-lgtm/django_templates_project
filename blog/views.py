from django.http import Http404
from django.shortcuts import render, get_object_or_404, reverse
from django.template.defaultfilters import slugify
from .models import Post, Category

def home(request):
    breadcrumb = [
        {'title': 'home', 'url': None}
    ]
    return render(request, 'blog/home_page.html', {'breadcrumb': breadcrumb})


def category(request, cat_slug):
    cat_name = Category.objects.get(slug=cat_slug).name
    breadcrumb = [
        {'title': 'home',
         'url': reverse('home')},
        {'title': cat_name,
         'url': None}
    ]
    return render(request, 'blog/home_page.html', {'cat_slug': cat_slug, 'breadcrumb': breadcrumb})


def post(request, cat_slug, post_slug):
    cat_name = Category.objects.get(slug=cat_slug).name
    post = Post.objects.get(slug=post_slug)
    breadcrumb = [
        {'title': 'home',
         'url': reverse('home')},
        {'title': cat_name,
         'url': reverse('cat', args=[cat_slug])},
        {'title': post.title,
         'url': None}
    ]
    return render(request, 'blog/home_page.html', {'cat_slug': cat_slug,
                                                                        'post_slug': post_slug,
                                                                        'breadcrumb': breadcrumb,
                                                                        'post': post,
                                                                        })