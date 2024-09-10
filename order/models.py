from django.conf import settings
from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('eSewa', 'eSewa'),
        ('cash_on_delivery', 'Cash on Delivery'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)

    totalQuantity = models.PositiveIntegerField(default=1)
    price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shippingCost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    orderStatus = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    orderDate = models.DateTimeField(auto_now_add=True)
    shippingAddress = models.CharField(max_length=225, blank=True)
    billingAddress = models.CharField(max_length=225, blank=True)
    paymentMethod = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICES, default='pending')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)

    # This is for any discount later in the product  
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    # This note is for the admin if any error occur he/she can send note to that order
    notes = models.TextField(blank=True, null=True)


    


    def __str__(self):
        return f"Order of {self.product.title} by {self.user.username} on {self.orderDate} is {self.orderStatus}"
    




