# Generated by Django 4.1 on 2022-11-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0018_alter_sefer_primary_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sefer",
            name="primary_category",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]