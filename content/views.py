from django.shortcuts import render
from .models import Post

posts = [
    {
        'title': 'first post',
        'author': 'me',
        'date_posted': 'march 1, 2020',
        'content': 'photo goes here',
    },
    {
        'title': 'second post',
        'author': 'me2',
        'date_posted': 'march 2, 2020',
        'content': 'second photo would go here',
    },
    {
        'title': 'third post',
        'author': 'me3',
        'date_posted': 'march 4, 2020',
        'content': 'third photo here',
    }
]

context = {
    'posts': posts
    #When posts created
    #'posts': Post.object.all()
}


def home(request):
    return render(request, 'content/home.html', context)


def about(request):
    return render(request, 'content/about.html')
