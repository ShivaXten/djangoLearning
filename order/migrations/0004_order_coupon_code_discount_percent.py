# Generated by Django 4.2.15 on 2024-09-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_coupon_alter_order_coupon_code_order_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Coupon_code_discount_percent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
