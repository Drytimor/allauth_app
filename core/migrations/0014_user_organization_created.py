# Generated by Django 4.2.7 on 2023-12-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_employees_user_alter_events_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization_created',
            field=models.BooleanField(default=False),
        ),
    ]