# Generated by Django 4.1 on 2022-08-10 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "website",
            "0002_sefer_order_bottom_order_chapfontsize_order_engfont_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="bottom",
        ),
        migrations.RemoveField(
            model_name="order",
            name="chapfontsize",
        ),
        migrations.RemoveField(
            model_name="order",
            name="engfont",
        ),
        migrations.RemoveField(
            model_name="order",
            name="evenhead",
        ),
        migrations.RemoveField(
            model_name="order",
            name="fontsize",
        ),
        migrations.RemoveField(
            model_name="order",
            name="headpos",
        ),
        migrations.RemoveField(
            model_name="order",
            name="hebboldfont",
        ),
        migrations.RemoveField(
            model_name="order",
            name="hebfont",
        ),
        migrations.RemoveField(
            model_name="order",
            name="inner",
        ),
        migrations.RemoveField(
            model_name="order",
            name="layout",
        ),
        migrations.RemoveField(
            model_name="order",
            name="newpage",
        ),
        migrations.RemoveField(
            model_name="order",
            name="oddhead",
        ),
        migrations.RemoveField(
            model_name="order",
            name="outer",
        ),
        migrations.RemoveField(
            model_name="order",
            name="pagenumheb",
        ),
        migrations.RemoveField(
            model_name="order",
            name="pagenumloc",
        ),
        migrations.RemoveField(
            model_name="order",
            name="parskip",
        ),
        migrations.RemoveField(
            model_name="order",
            name="spacing",
        ),
        migrations.RemoveField(
            model_name="order",
            name="top",
        ),
    ]