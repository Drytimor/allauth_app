# Generated by Django 4.2.7 on 2023-12-05 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sport', 'спорт'), ('tourism', 'туризм'), ('education', 'образование'), ('science', 'наука'), ('entertainment', 'развлечение'), ('sundry', 'разное')], max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to='core.categories', verbose_name='Категория')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.AddConstraint(
            model_name='categories',
            constraint=models.CheckConstraint(check=models.Q(('name__in', ['sport', 'tourism', 'education', 'science', 'entertainment', 'sundry'])), name='check_categories'),
        ),
    ]
