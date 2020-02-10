from django.shortcuts import render
from .models import Post,User
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='index.html'

class BlogDetailView(ListView):
