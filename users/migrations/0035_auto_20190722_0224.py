# Generated by Django 2.2.3 on 2019-07-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_userprofile_active'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['active'], name='users_userp_active_9fb6e2_idx'),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['ldap_id'], name='users_userp_ldap_id_1370fe_idx'),
        ),
    ]
