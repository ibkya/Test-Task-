# Generated by Django 5.1.2 on 2024-10-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="timeslot",
            name="camera_ids",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
