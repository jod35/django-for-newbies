from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=225)
    password=models.TextField()

    def __str__(self):
        return self.username
