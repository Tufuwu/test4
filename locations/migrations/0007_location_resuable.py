# Generated by Django 2.0.2 on 2018-03-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_auto_20180306_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='resuable',
            field=models.BooleanField(default=False),
        ),
    ]
