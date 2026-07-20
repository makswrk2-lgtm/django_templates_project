from django.shortcuts import render

def index(request):
    return render(request, 'blog/home_page.html')

def choice(request):
    return index(request)