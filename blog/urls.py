from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>', views.choice, name='nav_bar_choice'),
]
