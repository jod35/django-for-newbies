from django.shortcuts import render
from .models import Post,User
from .forms import PostForm


def home(request):
    posts=Post.objects.all()
    context={
    'posts':posts
    }
    return render(request,'blog/index.html',context)

def create_post(request):
    form=PostForm()
    users=User.objects.all()
    context={
    'form':form,
    'users':users

    }
    return render(request,'blog/new_post.html',context)
