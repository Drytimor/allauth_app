# Generated by Django 4.2.7 on 2023-12-18 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_remove_events_limit_clients_and_more'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordings',
            name='event',
        ),
        migrations.AddField(
            model_name='recordings',
            name='event_record',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to='organization.eventrecords', verbose_name='Мероприятие'),
            preserve_default=False,
        ),
    ]
