from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no_avatar.jpg')


class Statistics(models.Model):
    user = models.OneToOneField(User, related_name='statistics', on_delete=models.CASCADE)
    rating = models.IntegerField(default=1000)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    games_drawn = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Statistics.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.statistics.save()

# Create your models here.
