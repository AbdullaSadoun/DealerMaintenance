# Generated by Django 5.0.4 on 2024-04-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("service_name", models.CharField(max_length=200)),
                ("estimated_time", models.CharField(max_length=100)),
                (
                    "estimated_labour_cost",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]