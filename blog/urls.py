from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<slug:cat_slug>/', views.category, name='cat'),
    path('<slug:cat_slug>/<slug:post_slug>', views.post, name='post'),
]