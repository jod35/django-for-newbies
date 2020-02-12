from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=50)



class Employee(models.Model):
    full_name=models.CharField(max_length=200)
    emp_code=models.CharField(max_length=3)
    email=models.CharField(max_length=20)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    
