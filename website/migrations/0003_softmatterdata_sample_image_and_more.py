# Generated by Django 5.0.6 on 2024-07-01 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_alter_softmatterdata_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="softmatterdata",
            name="sample_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="softmatterdata",
            name="lastupdate",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 1, 4, 28, 36, 21595, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="softmatterdata",
            name="lock",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
