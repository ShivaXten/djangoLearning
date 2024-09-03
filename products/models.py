from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    # added more details for the users to see 
    discount_percentage = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    warranty_information = models.CharField(max_length=255, blank=True)
    shipping_information = models.CharField(max_length=255, blank=True)
    availability_status = models.CharField(max_length=100, default='In Stock')
    return_policy = models.CharField(max_length=255, blank=True)
    minimum_order_quantity = models.PositiveIntegerField(default=1)
    barcode = models.CharField(max_length=255, blank=True)
    qr_code = models.URLField(blank=True)
    
    

    

    def __str__(self):
        return self.title