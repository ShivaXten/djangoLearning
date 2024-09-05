import os
from django.db import models
from .productsUpdateCalculations import determine_availability_status ,calculate_discounted_price

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True)
    category = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    discount_percentage = models.FloatField(default=0)
    price_after_discount = models.FloatField(default=0)
    warranty_information = models.CharField(max_length=255, blank=True)
    shipping_information = models.CharField(max_length=255, blank=True)
    availability_status = models.CharField(max_length=100, default='In Stock')
    return_policy = models.CharField(max_length=255, blank=True)
    minimum_order_quantity = models.PositiveIntegerField(default=1)
    rating = models.FloatField(default=0)
    barcode = models.CharField(max_length=255, blank=True)
    qr_code = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        # Update availability_status using the function from calculations.py
        self.availability_status = determine_availability_status(self.price, self.stock)
        # update the discountAmount 
        self.price_after_discount = calculate_discounted_price(self.price, self.discount_percentage)
        
        # Call the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    



# This is for the dynamic path allocation according to the category of the product
def get_feature_image_upload_path(instance, filename):
    # Get the category of the associated product
    category = instance.product.category
    # Create a path based on the category
    return os.path.join('product_feature_images', category, filename)


# This is product feature image where admin can upload more then 1 image for that product 
class ProductFeatureImage(models.Model):
    product = models.ForeignKey(Product, related_name='feature_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_feature_image_upload_path)

    def __str__(self):
        return f'Image for {self.product.title}'
