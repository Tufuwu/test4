# Generated by Django 1.11.15 on 2018-09-25 15:42


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0118_auto_20180921_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='lead_capture_list_name',
            field=models.CharField(default='Master_default', help_text='The sailthru email list name to capture leads', max_length=255),
        ),
    ]
