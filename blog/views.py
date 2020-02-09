from django.shortcuts import render
from .models import Post,User

# Create your views here.

def home(request):

    posts=Post.objects.all()

    context={
    'posts':posts
    }

    return render(request,'blog/index.html',context)


def create_post(request):
    context={}
    return render(request,'blog/new_post.html',context)
