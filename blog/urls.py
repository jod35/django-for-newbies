from django.urls import path
from . import views

urlpatterns=[
  path('blog',views.home,name='blog_home'),
]
