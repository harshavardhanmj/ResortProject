# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20180426_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datepicker2',
            field=models.DateField(null=True),
        ),
    ]
