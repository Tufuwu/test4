# Generated by Django 2.2.9 on 2020-06-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjallocation', '0008_auto_20181019_2059'),
        ('participants', '0013_rename_test_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adjudicator',
            old_name='conflicts',
            new_name='team_conflicts',
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='team_conflicts',
            field=models.ManyToManyField(related_name='adj_team_conflicts', through='adjallocation.AdjudicatorTeamConflict', to='participants.Team', verbose_name='team conflicts'),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='adjudicator_conflicts',
            field=models.ManyToManyField(related_name='adj_adj_conflicts', through='adjallocation.AdjudicatorAdjudicatorConflict', to='participants.Adjudicator', verbose_name='adjudicator conflicts'),
        ),
        migrations.AddField(
            model_name='team',
            name='institution_conflicts',
            field=models.ManyToManyField(related_name='team_inst_conflicts', through='adjallocation.TeamInstitutionConflict', to='participants.Institution', verbose_name='institution conflicts'),
        ),
    ]
