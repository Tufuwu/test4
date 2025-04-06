# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carapplication',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carapplication',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
