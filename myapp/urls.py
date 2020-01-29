from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('pages/',include('pages.urls')),
    path('admin/', admin.site.urls),
]
