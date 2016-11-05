from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=32)
    start_pos = models.CharField(max_length=512)
    question = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    difficulty = models.DecimalField(default=1.0, decimal_places=2, max_digits=3)


# Create your models here.
