# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-01 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0008_auto_20161124_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='user_detail',
        ),
    ]
