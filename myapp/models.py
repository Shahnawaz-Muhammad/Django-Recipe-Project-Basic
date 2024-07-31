from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
