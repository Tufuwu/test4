# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-05 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4comments', '0003_comment_comment_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=4000),
        ),
    ]
