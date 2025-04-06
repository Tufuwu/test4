# Generated by Django 2.0.2 on 2018-05-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0012_auto_20171009_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='expires',
            field=models.DateTimeField(blank=True, help_text='Used to override the content of the Give Sticky. Set the content below to change.', null=True),
        ),
    ]
