# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20161204_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='difficulty',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=3),
        ),
    ]
