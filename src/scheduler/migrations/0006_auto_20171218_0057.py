# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-17 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20171218_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledemailaction',
            name='subject',
            field=models.CharField(default='', max_length=2048, verbose_name='Email subject'),
        ),
    ]