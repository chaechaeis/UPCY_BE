# Generated by Django 5.1.1 on 2024-09-20 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("market", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="market",
            name="reformer",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="market",
                to="users.reformerprofile",
            ),
        ),
        migrations.AddField(
            model_name="marketservice",
            name="market",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="market_service",
                to="market.market",
            ),
        ),
        migrations.AddField(
            model_name="servicematerial",
            name="market_service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_material",
                to="market.marketservice",
            ),
        ),
        migrations.AddField(
            model_name="serviceoption",
            name="market_service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_option",
                to="market.marketservice",
            ),
        ),
        migrations.AddField(
            model_name="servicestyle",
            name="market_service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_style",
                to="market.marketservice",
            ),
        ),
    ]
