# Generated by Django 5.1.1 on 2024-09-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_reformerportfolio_reformer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reformer",
            name="reformer_area",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
