# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-20 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dis', '0008_auto_20190920_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='time_create',
            field=models.DateField(auto_now_add=True, help_text='格式yyyy-mm-dd', null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='time_update',
            field=models.DateField(auto_now_add=True, help_text='格式yyyy-mm-dd', null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='time_create',
            field=models.DateField(blank=True, default=None, help_text='格式yyyy-mm-dd', null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='time_update',
            field=models.DateField(auto_now_add=True, help_text='格式yyyy-mm-dd', null=True, verbose_name='更新时间'),
        ),
    ]
