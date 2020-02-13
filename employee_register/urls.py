from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list,name='emloyee_list'),
    path('add/',views.employee_form,name='employee_form'),
    path('delete/',views.emaployee_delete,name='employee_delete')
]