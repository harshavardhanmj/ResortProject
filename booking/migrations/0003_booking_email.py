# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180426_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=320, null=True),
        ),
    ]