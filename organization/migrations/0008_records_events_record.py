# Generated by Django 4.2.7 on 2023-12-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_delete_eventrecords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_clients', models.SmallIntegerField()),
                ('quantity_clients', models.SmallIntegerField(default=0)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'records',
            },
        ),
        migrations.AddField(
            model_name='events',
            name='record',
            field=models.ManyToManyField(null=True, related_name='events', to='organization.records'),
        ),
    ]
