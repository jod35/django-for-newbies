from django.urls import path
from . import views

urlpatterns=[
  path('new/',views.create_post,name='blog_new'),
  path('',views.home,name='blog_home'),
]
