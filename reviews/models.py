from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reviewer_name = models.CharField(max_length=255)
    reviewer_email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.product.title}"
