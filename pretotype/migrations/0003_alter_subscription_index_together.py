# Generated by Django 4.2.3 on 2023-08-01 05:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pretotype", "0002_subscription_referer"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="subscription",
            index_together={("email", "referer")},
        ),
    ]
