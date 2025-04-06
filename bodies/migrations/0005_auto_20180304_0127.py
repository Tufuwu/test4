# Generated by Django 2.0.2 on 2018-03-03 19:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('bodies', '0004_merge_20180303_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='followers',
            field=models.ManyToManyField(related_name='followed_bodies', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='body',
            name='events',
            field=models.ManyToManyField(related_name='bodies', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='bodychildrelation',
            name='child',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='bodies.Body'),
        ),
        migrations.AlterField(
            model_name='bodychildrelation',
            name='parent',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bodies.Body'),
        ),
    ]
