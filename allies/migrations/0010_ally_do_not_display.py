# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allies', '0009_auto_20160922_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='ally',
            name='do_not_display',
            field=models.BooleanField(default=False),
        ),
    ]
