# Generated by Django 4.2.7 on 2023-12-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_events_is_active_dateevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('event', models.ManyToManyField(related_name='event_records', to='organization.events')),
            ],
            options={
                'db_table': 'event_records',
            },
        ),
        migrations.DeleteModel(
            name='DateEvents',
        ),
    ]