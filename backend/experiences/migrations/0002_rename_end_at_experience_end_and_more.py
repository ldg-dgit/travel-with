# Generated by Django 4.1.1 on 2022-10-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="experience",
            old_name="end_at",
            new_name="end",
        ),
        migrations.RenameField(
            model_name="experience",
            old_name="start_at",
            new_name="start",
        ),
        migrations.AlterField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="perk",
            name="explanation",
            field=models.TextField(blank=True, null=True),
        ),
    ]
