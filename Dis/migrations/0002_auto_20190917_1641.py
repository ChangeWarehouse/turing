# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-17 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='repassword',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='sex',
        ),
    ]