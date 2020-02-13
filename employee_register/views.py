from django.shortcuts import render

# Create your views here.

def employee_list(request):
    return render(request,'employee_register/employee_list.html')

def employee_form(request):
    return render(request,'employee_register/employee_register.html')

def emaployee_delete(request):
    return