# Generated by Django 4.1.2 on 2022-11-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_order_meals_order_meals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
