# Generated by Django 2.1.5 on 2019-01-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_refresh',
            field=models.DateTimeField(default='1970-01-01T00:00:00Z'),
        ),
    ]
