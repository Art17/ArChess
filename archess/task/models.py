from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    start_pos = models.CharField(max_length=512)
    answer = models.CharField(max_length=512)
    likes = models.IntegerField(default=0)
    difficulty = models.DecimalField(default=1.0, decimal_places=2, max_digits=3)


# Create your models here.
