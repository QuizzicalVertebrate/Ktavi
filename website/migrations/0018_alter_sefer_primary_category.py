# Generated by Django 4.1 on 2022-11-06 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_translation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sefer",
            name="primary_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pc",
                to="website.primarycategory",
            ),
        ),
    ]
