# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0011_auto_20170705_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageelement',
            name='order',
        ),
    ]
