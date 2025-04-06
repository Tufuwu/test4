# Generated by Django 1.11.15 on 2019-01-24 15:49


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0146_remove_log_queries_switch'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='hubspot_lead_capture_form_id',
            field=models.CharField(help_text='The Hubspot form ID for the lead capture form', max_length=128, null=True),
        ),
    ]
