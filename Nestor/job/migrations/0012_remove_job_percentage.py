# Generated by Django 4.2.11 on 2024-05-15 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_remove_favoritejob_applicant_favoritejob_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='percentage',
        ),
    ]
