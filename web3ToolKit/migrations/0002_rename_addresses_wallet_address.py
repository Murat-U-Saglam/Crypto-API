# Generated by Django 4.1.2 on 2022-10-29 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web3ToolKit", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallet",
            old_name="addresses",
            new_name="address",
        ),
    ]
