# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170421_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comment_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='message_bad',
            field=models.TextField(blank=True, verbose_name='Default message to bad changesets'),
        ),
        migrations.AddField(
            model_name='user',
            name='message_good',
            field=models.TextField(blank=True, verbose_name='Default message to good changesets'),
        ),
    ]
