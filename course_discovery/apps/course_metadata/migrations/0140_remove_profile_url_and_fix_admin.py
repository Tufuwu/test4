# Generated by Django 1.11.15 on 2018-12-12 20:30


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0139_drupalpublishuuidconfig_push_people'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personareaofexpertise',
            options={'verbose_name_plural': 'Person Areas of Expertise'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='profile_url',
        ),
    ]
