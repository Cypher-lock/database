# Generated by Django 5.0.6 on 2024-07-02 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0009_delete_compositiontypes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compositions",
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
                ("composition", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "comps",
                "managed": True,
            },
        ),
        migrations.AlterField(
            model_name="softmatterdata",
            name="composition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="website.compositions",
            ),
        ),
    ]
