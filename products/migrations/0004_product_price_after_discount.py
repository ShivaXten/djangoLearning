# Generated by Django 4.2.15 on 2024-09-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productfeatureimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_after_discount',
            field=models.FloatField(default=0),
        ),
    ]
