# Generated by Django 5.1.1 on 2024-09-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0008_alter_service_basic_price_alter_service_max_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceoption",
            name="option_price",
            field=models.PositiveIntegerField(),
        ),
    ]