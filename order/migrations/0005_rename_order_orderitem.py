# Generated by Django 4.2.15 on 2024-09-16 05:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_alter_product_price'),
        ('order', '0004_order_coupon_code_discount_percent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderItem',
        ),
    ]
