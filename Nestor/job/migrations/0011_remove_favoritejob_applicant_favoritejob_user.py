# Generated by Django 4.2.11 on 2024-05-15 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0010_alter_application_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritejob',
            name='applicant',
        ),
        migrations.AddField(
            model_name='favoritejob',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
