# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0033_suspicionreasons_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspicionreasons',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
