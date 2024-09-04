import os
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()
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
