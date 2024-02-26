from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
       'author': '<NAME>',
       'title': 'My first blog',
        'content': 'This is my first blog',
        'date_posted': 'January 31. 2024'


    },
    {
       'author': 'Alice',
       'title': 'My first blog',
        'content': 'This is my first blog',
        'date_posted': 'January 23. 2024'


    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/home.html', context)

# Create your views here.

def about(request):
    return render (request, 'blog/about.html', {'title': 'About me' })