from django import template
from django.shortcuts import get_object_or_404
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/includes/menu.html')
def show_menu():
    posts = Post.objects.filter(is_published=1).only('title', 'get_absolute_url')
    return {
        'menu': posts
    }