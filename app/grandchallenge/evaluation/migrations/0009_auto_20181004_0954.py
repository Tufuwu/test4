# Generated by Django 2.0.8 on 2018-10-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("evaluation", "0008_config_submission_join_key")]

    operations = [
        migrations.AddField(
            model_name="config",
            name="publication_url_choice",
            field=models.CharField(
                choices=[
                    ("off", "Off"),
                    ("opt", "Optional"),
                    ("req", "Required"),
                ],
                default="off",
                help_text="Show a publication url field on the submission page so that users can submit a link to a publication that corresponds to their submission. Off turns this feature off, Optional means that including the url is optional for the user, Required means that the user must provide an url.",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="config",
            name="score_decimal_places",
            field=models.PositiveSmallIntegerField(
                default=4,
                help_text="The number of decimal places to display for the score",
            ),
        ),
        migrations.AddField(
            model_name="config",
            name="show_publication_url",
            field=models.BooleanField(
                default=False,
                help_text="Show a link to the publication on the results page",
            ),
        ),
        migrations.AddField(
            model_name="config",
            name="supplementary_file_choice",
            field=models.CharField(
                choices=[
                    ("off", "Off"),
                    ("opt", "Optional"),
                    ("req", "Required"),
                ],
                default="off",
                help_text="Show a supplementary file field on the submissions page so that users can upload an additional file along with their predictions file as part of their submission (eg, include a pdf description of their method). Off turns this feature off, Optional means that including the file is optional for the user, Required means that the user must upload a supplementary file.",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="publication_url",
            field=models.URLField(
                blank=True,
                help_text="A URL for the publication associated with this submission.",
            ),
        ),
    ]
