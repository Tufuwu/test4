# Generated by Django 3.0.4 on 2020-11-05 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0052_pagelogentry'),
        ('pages', '0003_merge_20200930_1001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoverPage',
        ),
    ]
