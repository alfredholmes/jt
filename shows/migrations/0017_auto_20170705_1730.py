# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0016_auto_20170705_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageelement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imageelement',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
