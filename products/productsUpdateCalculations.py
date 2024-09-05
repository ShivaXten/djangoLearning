# This is to calculate the product stock availability 
def determine_availability_status(price, stock):
    if stock == 0:
        return 'Out of Stock'
    elif price > 95000 and stock < 5:
        return 'Low Stock'
    elif 35000 <= price <= 95000 and stock < 10:
        return 'Low Stock'
    elif 0 <= price < 35000 and stock < 20:
        return 'Low Stock'
    else:
        return 'In Stock'
    
# This is to calculate the discount amount 
def calculate_discounted_price(price, discount_percentage):
    if discount_percentage > 100:
        discount_percentage = 100
    discount_amount = (price * discount_percentage) / 100
    return price - discount_amount
