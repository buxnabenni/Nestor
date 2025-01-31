# Generated by Django 4.2.11 on 2024-05-11 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_date_of_offering'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_of_offering',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='job',
            name='num_of_applicants',
            field=models.IntegerField(default=0),
        ),
    ]
