from django import template
from blog.data import menu_db

register = template.Library()

menu_db = sorted(menu_db, key=lambda x: x['id'], reverse=True)

@register.inclusion_tag('blog/includes/menu.html')
def show_menu():
    return {
        'menu': menu_db
    }