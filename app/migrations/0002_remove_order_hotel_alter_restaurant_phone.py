# Generated by Django 4.1.2 on 2022-11-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='hotel',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]