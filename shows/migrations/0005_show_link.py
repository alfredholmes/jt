# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_show_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='link',
            field=models.CharField(default='gangstergranny', max_length=200),
            preserve_default=False,
        ),
    ]
