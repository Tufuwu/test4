# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-30 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0040_auto_20170328_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspicionreasons',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
