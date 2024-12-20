# Generated by Django 5.1.1 on 2024-09-27 02:13

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_reformer_reformer_area"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reformerawards",
            name="id",
        ),
        migrations.RemoveField(
            model_name="reformercareer",
            name="id",
        ),
        migrations.RemoveField(
            model_name="reformercertification",
            name="id",
        ),
        migrations.RemoveField(
            model_name="reformereducation",
            name="id",
        ),
        migrations.RemoveField(
            model_name="reformerfreelancer",
            name="id",
        ),
        migrations.AddField(
            model_name="reformerawards",
            name="award_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AddField(
            model_name="reformercareer",
            name="career_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AddField(
            model_name="reformercertification",
            name="certification_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AddField(
            model_name="reformereducation",
            name="education_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AddField(
            model_name="reformerfreelancer",
            name="freelancer_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
