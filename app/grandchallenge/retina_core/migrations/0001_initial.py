# Generated by Django 2.1.3 on 2018-12-07 15:50

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import migrations


def create_retina_groups_forward(apps, schema_editor):
    # You would want to get the historical models for Group, but this does not seem to work
    # User = apps.get_model("auth", "User")

    # Create retina admin and grader groups
    Group.objects.create(name=settings.RETINA_GRADERS_GROUP_NAME)
    Group.objects.create(name=settings.RETINA_ADMINS_GROUP_NAME)


def create_retina_groups_backward(apps, schema_editor):
    # You would want to get the historical models for Group, but this does not seem to work
    # User = apps.get_model("auth", "User")

    # Remove retina admin and grader groups
    Group.objects.get(name=settings.RETINA_GRADERS_GROUP_NAME).delete()
    Group.objects.get(name=settings.RETINA_ADMINS_GROUP_NAME).delete()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(
            create_retina_groups_forward, create_retina_groups_backward
        )
    ]
