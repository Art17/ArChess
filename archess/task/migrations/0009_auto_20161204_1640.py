# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0008_auto_20161204_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
