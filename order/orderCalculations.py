

# Calculate total 
def calculate_total_price(total_quantity, product_price, shipping_cost):
     return (total_quantity * product_price) + shipping_cost


def calculate_amount_after_discount(Product_Discount_Percent,product_price,coupon_code,totalQuantity):
        return(((Product_Discount_Percent+coupon_code)*product_price)/100)*totalQuantity

