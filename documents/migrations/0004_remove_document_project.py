# Generated by Django 4.2.7 on 2023-12-28 23:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0003_document_access_level_document_shared_with"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="project",
        ),
    ]
