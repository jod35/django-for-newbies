from django.urls import path
from .views import BlogListView

urlpatterns=[
  path('new/',views.create_post,name='blog_new'),
  path('',BlogListView.as_view(),name='blog_home'),
]
