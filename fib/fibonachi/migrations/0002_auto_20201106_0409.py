# Generated by Django 3.1.2 on 2020-11-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fibonachi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fibonachi",
            name="number_input",
            field=models.IntegerField(verbose_name="Исходное число"),
        ),
    ]
