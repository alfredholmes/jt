# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20170704_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='category',
        ),
    ]
