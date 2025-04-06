# Generated by Django 1.10.7 on 2017-09-05 22:20


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("utils", "0013_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hat",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40, unique=True, verbose_name="Casquette")),
            ],
            options={
                "verbose_name": "Casquette",
                "verbose_name_plural": "Casquettes",
            },
        ),
        migrations.CreateModel(
            name="HatRequest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("hat", models.CharField(max_length=40, verbose_name="Casquette")),
                ("reason", models.TextField(max_length=3000, verbose_name="Raison de la demande")),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="request_date", db_index=True, verbose_name="Date de la demande"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requested_hats",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Demande de casquette",
                "verbose_name_plural": "Demandes de casquettes",
            },
        ),
        migrations.AddField(
            model_name="comment",
            name="hat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comments",
                to="utils.Hat",
                verbose_name="Casquette",
            ),
        ),
    ]
