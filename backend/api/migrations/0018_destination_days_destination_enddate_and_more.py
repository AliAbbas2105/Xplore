# Generated by Django 5.1.3 on 2024-11-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_destination_destinationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='Days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='destination',
            name='EndDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='destinations/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='MaxTravellers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='Nights',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='destination',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='StartDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
