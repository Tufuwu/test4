# Generated by Django 2.2 on 2020-06-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_make_not_null_with_django_default", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="a",
            name="col",
            field=models.CharField(default="empty", max_length=10),
        ),
    ]
