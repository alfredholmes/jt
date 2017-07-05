# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0009_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageelement',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='link',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='link',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
