# Generated by Django 4.2.7 on 2023-12-08 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_role_alter_organizations_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Customers',
        ),
    ]