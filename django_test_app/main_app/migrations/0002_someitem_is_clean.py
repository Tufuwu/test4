# -*- coding: utf-8 -*-
# Generated by Django 2.2.7 on 2019-11-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration to add ``is_clean`` field to ``SomeItem``."""

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='someitem',
            name='is_clean',
            field=models.BooleanField(default=True),
        ),
    ]
