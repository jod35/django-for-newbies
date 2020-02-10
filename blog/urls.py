from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='blog_home'),
  path('new_post',views.create_post,name='blog_new')
]
