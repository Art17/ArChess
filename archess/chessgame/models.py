from django.db import models
from django.contrib.auth.models import User


class ChessGame(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
