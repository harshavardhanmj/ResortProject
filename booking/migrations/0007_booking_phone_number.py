# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20180427_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
