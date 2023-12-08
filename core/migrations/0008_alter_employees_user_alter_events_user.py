# Generated by Django 4.2.7 on 2023-12-08 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_employees_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='events',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
