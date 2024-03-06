# Generated by Django 5.0.2 on 2024-03-05 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
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
                ("title", models.CharField(max_length=255)),
                ("scheduled_time", models.DateTimeField()),
                (
                    "duration",
                    models.PositiveIntegerField(help_text="Duration in minutes"),
                ),
                ("agenda", models.TextField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("outcomes", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "access_level",
                    models.CharField(
                        choices=[
                            ("read", "Read"),
                            ("write", "Write"),
                            ("edit", "Edit"),
                        ],
                        default="read",
                        max_length=100,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_meetings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        related_name="meetings", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meetings",
                        to="projects.project",
                    ),
                ),
                (
                    "shared_with",
                    models.ManyToManyField(
                        blank=True,
                        related_name="meeting_participants",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Meeting",
                "verbose_name_plural": "Meetings",
                "ordering": ["-scheduled_time", "title"],
            },
        ),
    ]
