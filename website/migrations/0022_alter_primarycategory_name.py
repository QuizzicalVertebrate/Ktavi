# Generated by Django 4.1 on 2022-11-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0021_alter_sefer_prime_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primarycategory",
            name="name",
            field=models.CharField(
                default="we have a miss here", max_length=50, unique=True
            ),
        ),
    ]