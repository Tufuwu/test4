# Generated by Django 2.0.13 on 2019-07-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0033_auto_20190701_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errata',
            name='resource',
            field=models.CharField(blank=True, choices=[('Textbook', 'Textbook'), ('iBooks version', 'iBooks version'), ('Instructor solution manual', 'Instructor solution manual'), ('Student solution manual', 'Student solution manual'), ('OpenStax Tutor', 'OpenStax Tutor'), ('OpenStax Concept Coach', 'OpenStax Concept Coach'), ('Rover by OpenStax', 'Rover by OpenStax'), ('OpenStax + SE', 'OpenStax + SE'), ('Kindle', 'Kindle'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
