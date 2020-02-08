from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=225)
    password=models.TextField()

    def __str__(self):
        return self.username


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
