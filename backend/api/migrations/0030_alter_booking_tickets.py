# Generated by Django 5.1.3 on 2024-11-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_booking_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Tickets',
            field=models.IntegerField(),
        ),
    ]
