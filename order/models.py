from django.conf import settings
from django.db import models
from products.models import Product
from .orderCalculations import calculate_total_price,calculate_amount_after_discount,get_shipping_cost


# This is for the admin to set the location 
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.name} - {self.price}"
    


class Order(models.Model):

    # LOCATION_CHOICES =[
    #     ('parsyang','50'),
    #     ('amarsingh','60'),
    #     ('birauta','40'),
    #     ('bindabasini','45'),
    #     ('bhalam','80'),
    #     ('manipal','60'),
    #     ('lekhnath','45'),
    #     ('lakeside','80'),
    #     ('outofvalley','500'),
    #     ('shop','20')
        
    # ]
    
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
    location = models.ForeignKey(Location, related_name='orders', on_delete=models.SET_NULL, null=True, blank=True)

    totalQuantity = models.PositiveIntegerField(default=1)
    price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shippingCost = models.PositiveIntegerField(default=0)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    orderStatus = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    orderDate = models.DateTimeField(auto_now_add=True)
    shippingAddress = models.CharField(max_length=225, blank=True )
    billingAddress = models.CharField(max_length=225, blank=True)
    paymentMethod = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICES, default='pending')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)

    # This is for any discount later in the product  
    coupon_code = models.PositiveIntegerField(default=0)
    # This note is for the admin if any error occur he/she can send note to that order
    notes = models.TextField(blank=True, null=True)


    def save(self, *args, **kwargs):
       
        if self.product:
            product_price = self.product.price
            Product_Discount_Percent=self.product.discount_percentage

            self.shippingCost = get_shipping_cost(self.shippingAddress)
            self.totalPrice = calculate_total_price(Product_Discount_Percent,product_price,self.coupon_code,self.totalQuantity, self.shippingCost)
            self.price_after_discount = calculate_amount_after_discount (Product_Discount_Percent,product_price,self.coupon_code,self.totalQuantity)     
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Order of {self.product.title} by {self.user.username} on {self.orderDate} is {self.orderStatus}"
    

