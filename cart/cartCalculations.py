from .models import Cart, Product
from django.db.models import Sum, F


# This is the calculation done for the cart so that backend can handel all
def calculate_totals(user):
    carts = Cart.objects.filter(user=user) 
    total_quantity = carts.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    total_products = carts.count()
    
    # Calculate total price
    total = carts.aggregate(
        total=Sum(F('price'))
    )['total'] or 0

    # Calculate total discounted price
    discounted_total = carts.aggregate(
        discounted_total=Sum(F('discounted_price'))
    )['discounted_total'] or 0
    return {
        'total': total,
        'discounted_total': discounted_total,
        'total_quantity': total_quantity,
        'total_products': total_products
    }



# This is to check the available stocks
def check_stock(product_id, quantity):
    try:
        product = Product.objects.get(id=product_id)
        return product.stock >= quantity
    except Product.DoesNotExist:
        return False
