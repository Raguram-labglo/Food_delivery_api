# Generated by Django 4.1.2 on 2022-11-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_order_meals_alter_order_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant'),
        ),
    ]