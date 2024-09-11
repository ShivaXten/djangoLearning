

# Calculate total 
def calculate_amount_after_discount(Product_Discount_Percent,product_price,coupon_code,totalQuantity):
        return(product_price-(((Product_Discount_Percent+coupon_code)*product_price)/100))*totalQuantity


def calculate_total_price(Product_Discount_Percent,product_price,coupon_code,totalQuantity, shipping_cost):
     return ((product_price-(((Product_Discount_Percent+coupon_code)*product_price)/100))*totalQuantity)+shipping_cost

# This is to check and assign the shipping_cost which will be manage by the admin

def get_shipping_cost(shipping_address):
    from .models import Location  
    try:
        location = Location.objects.get(name__icontains=shipping_address)
        return location.price
    except Location.DoesNotExist:
        return 50   
