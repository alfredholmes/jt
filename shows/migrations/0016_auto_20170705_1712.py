# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0015_auto_20170705_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageelement',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Show'),
        ),
    ]