# Generated by Django 4.1.2 on 2022-11-28 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_profile_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transport',
        ),
    ]
