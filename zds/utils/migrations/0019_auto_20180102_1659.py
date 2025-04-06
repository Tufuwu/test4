# Generated by Django 1.10.8 on 2018-01-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("utils", "0018_auto_20171006_2126"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "ordering": ["position", "title"],
                "verbose_name": "Sous-categorie",
                "verbose_name_plural": "Sous-categories",
            },
        ),
        migrations.AddField(
            model_name="subcategory",
            name="position",
            field=models.IntegerField(db_index=True, default=0, verbose_name="Position"),
        ),
    ]
