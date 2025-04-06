# Generated by Django 2.0.2 on 2018-06-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0013_auto_20180515_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='expires',
            field=models.DateTimeField(blank=True, help_text='Set the date to override the content of the Give Sticky. Set the content below to change.', null=True),
        ),
    ]
