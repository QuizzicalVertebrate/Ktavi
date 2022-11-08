# Generated by Django 4.1 on 2022-08-22 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_primarycategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecondaryCategory",
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
                (
                    "name",
                    models.CharField(default="we have a mistake here", max_length=50),
                ),
                (
                    "primary_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="secondary_category",
                        to="website.primarycategory",
                    ),
                ),
            ],
        ),
    ]
