# Generated by Django 4.1.2 on 2022-10-29 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="wallet",
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
                ("addresses", models.CharField(max_length=36)),
                ("token", models.CharField(max_length=16)),
                (
                    "transactionValue",
                    models.DecimalField(decimal_places=0, max_digits=100),
                ),
                ("date", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]