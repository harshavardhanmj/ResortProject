# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecustomer', '0002_auto_20180421_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='StayConnected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
