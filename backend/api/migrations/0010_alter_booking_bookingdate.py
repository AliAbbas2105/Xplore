# Generated by Django 5.1.3 on 2024-11-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_destination_tour_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
