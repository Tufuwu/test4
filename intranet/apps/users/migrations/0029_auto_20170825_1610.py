# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20170824_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='primary_email',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.Photo'),
        ),
    ]
