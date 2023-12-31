# Generated by Django 4.2.3 on 2023-07-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                ("email", models.EmailField(max_length=254, verbose_name="이메일")),
                ("reg_ts", models.DateTimeField(auto_now=True, verbose_name="생성일시")),
            ],
            options={
                "verbose_name": "사전구독",
                "db_table": "pre_subscription",
            },
        ),
    ]
