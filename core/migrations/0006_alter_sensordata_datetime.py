# Generated by Django 5.0.6 on 2024-10-06 18:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sensordata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
