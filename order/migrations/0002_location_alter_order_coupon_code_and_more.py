# Generated by Django 4.2.15 on 2024-09-11 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='coupon_code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentMethod',
            field=models.CharField(choices=[('eSewa', 'eSewa'), ('cash_on_delivery', 'Cash on Delivery'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingCost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='order.location'),
        ),
    ]
