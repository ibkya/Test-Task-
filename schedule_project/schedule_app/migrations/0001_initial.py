# Generated by Django 5.1.2 on 2024-10-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_of_week", models.CharField(max_length=9)),
                ("start_time", models.TimeField()),
                ("stop_time", models.TimeField()),
                ("ids", models.JSONField()),
            ],
        ),
    ]
