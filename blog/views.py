from django.shortcuts import render
from .models import Post,User

# Create your views here.

def home(request):

    posts=Post.objects.all()

    context={
    'posts':posts
    }

    return render(request,'blog/index.html',context)
