# Generated by Django 2.0.13 on 2019-08-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0015_adoptionopportunityrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionopportunityrecord',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
