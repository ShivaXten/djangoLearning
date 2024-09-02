from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    

    

    def __str__(self):
        return self.title