# Generated by Django 5.1.3 on 2024-11-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_destination_googlemapsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='GoogleMapsLink',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
