# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0009_auto_20161204_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
