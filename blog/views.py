from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
   {
   'author':"Ssali JOnathan",
   'title':"Blog Post 1",
   'content':"First Content ",
   'date_posted':"Aug 27 2019",
   },
    {
    'author':"Nassali Jannet",
    'title':"Blog Post 2",
    'content':"Second Content ",
    'date_posted':"Aug 27 2019",
    }
]

def home(request):
    context={
    'posts':posts,
    'title':"Home Page"
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
