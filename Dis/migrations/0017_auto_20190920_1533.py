# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-20 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dis', '0016_auto_20190920_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pic_vid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dis.Videos', verbose_name='视频'),
        ),
    ]
