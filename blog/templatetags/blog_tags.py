from django import template
from django.shortcuts import get_object_or_404
from unicodedata import category
from django.db.models import Count

from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/includes/menu.html')
def show_cat_menu(cat_slug=None):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0).order_by('-total')
    return {
        'menu': cats,
        'cat_slug': cat_slug,
    }

@register.inclusion_tag('blog/includes/posts_list.html')
def show_posts_list(cat_slug, post_slug=None):
    posts = Post.published.select_related('category').filter(category__slug=cat_slug)
    return {'posts': posts,
            'post_slug': post_slug,}


@register.inclusion_tag('blog/includes/post_info.html')
def show_post_info(post):
    return {'post': post}


@register.simple_tag()
def get_posts():
    return Post.published.all().select_related('category')