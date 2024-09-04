from django.db.models import Avg
# This import is not needed because it is already in the relation with the product in model using OMR
from products.models import Product

def update_product_rating(product):
    # Calculate the average rating for the given product
    average_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
    new_rating = average_rating if average_rating is not None else 0
    
    # Only update if the rating has changed
    if product.rating != new_rating:
        product.rating = new_rating
        product.save()
