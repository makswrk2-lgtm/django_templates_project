from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page/', views.choice, name='nav_bar_choice'),
]
