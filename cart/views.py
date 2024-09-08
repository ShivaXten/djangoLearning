from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, Product
from .serializers import CartSerializer
from .cartCalculations import calculate_totals, check_stock




@api_view(['GET'])
def cart_overview(request):
    cart_urls = {
        'List all cart items for current user': 'current/',
        'Display cart by ID  only Current users cart': '<cart_id>/',
        'Add a product to the cart': 'addProduct/<product_id>/',
        'Update a cart item': 'update/<cart_id>/',
        'Delete a cart item': 'delete/<cart_id>/',
    }
    return Response(cart_urls)




# This is to display the current all items of the cart all models are simple and same 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_list(request):
    try:
        carts = Cart.objects.filter(user=request.user)
        if carts.exists():
            # Calculate aggregated data
            totals = calculate_totals(request.user)

            # Serialize the cart data with detailed product information
            serialized_carts = CartSerializer(carts, many=True).data

            response_data = {
                'carts': serialized_carts,
                'total': totals['total'],
                'discountedTotal': totals['discounted_total'],
                'userId': request.user.id,
                'totalProducts': totals['total_products'],
                'totalQuantity': totals['total_quantity']
            }
            return Response(response_data)
        else:
            return Response({'message': 'No carts found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)





# This is to get the Product by id only the user who has create the cartProduct item can get the cartItem by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(id=pk, user=request.user)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=404)

    serializer = CartSerializer(cart)
    return Response(serializer.data)





# This is to add the product in the cart .if you send product again and again it will add the quantity default is 1
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.data.get('quantity', 1))  # Default quantity is 1 if not provided

    if not check_stock(product_id, quantity):
        return Response({'error': 'Not enough stock available'}, status=400)

    cart, created = Cart.objects.get_or_create(user=request.user, product=product)

    if created:
        # New item in the cart
        cart.quantity = quantity
        cart.price = product.price * quantity
        cart.discounted_price = product.price_after_discount * quantity
    else:
        # Existing item in the cart
        new_quantity = cart.quantity + quantity
        if new_quantity > product.stock:
            return Response({'error': 'Not enough stock available'}, status=400)
        cart.quantity = new_quantity
        cart.price = product.price * new_quantity
        cart.discounted_price = product.price_after_discount * new_quantity

    cart.save()

    serializer = CartSerializer(cart)
    # Recalculate totals after adding/updating the cart
    totals = calculate_totals(request.user)
    
    return Response({
        'cart': serializer.data,
        'message': 'Product added/updated in cart',
        'total': totals['total'],
        'discountedTotal': totals['discounted_total'],
        'totalQuantity': totals['total_quantity'],
        'totalProducts': totals['total_products']
    })






#This is to update the cartItem if it is available in the cart 
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, pk):
    cart = get_object_or_404(Cart, pk=pk, user=request.user)
    serializer = CartSerializer(cart, data=request.data, partial=True)
    if serializer.is_valid():
        updated_cart = serializer.save()

        if updated_cart.quantity <= 0:
            return Response({'error': 'Quantity must be greater than zero'}, status=400)

        product = updated_cart.product
        if updated_cart.quantity > product.stock:
            return Response({'error': 'Insufficient stock'}, status=400)

        # Update price and discounted price based on new quantity
        updated_cart.price = product.price * updated_cart.quantity
        updated_cart.discounted_price = product.price_after_discount * updated_cart.quantity
        updated_cart.save()
        
        totals = calculate_totals(request.user)  # Recalculate totals
        response_data = {
            'cart': CartSerializer(updated_cart).data,
            'total': totals['total'],
            'discountedTotal': totals['discounted_total'],
            'totalQuantity': totals['total_quantity'],
            'totalProducts': totals['total_products']
        }
        return Response(response_data)
    return Response(serializer.errors, status=400)





# This is to delete the cartItem by passing the id of the cart  
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cart_item(request, pk):
    try:
        cart = Cart.objects.get(pk=pk, user=request.user)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=404)

    #This is to store the deleted item
    deleted_item_details = CartSerializer(cart).data
    cart.delete()
    totals = calculate_totals(request.user)  # Recalculate totals after deletion
    return Response({
        'message': 'Cart item deleted successfully',
        'cart': deleted_item_details,
        'total': totals['total'],
        'discountedTotal': totals['discounted_total'],
        'totalQuantity': totals['total_quantity'],
        'totalProducts': totals['total_products']
    }, status=200)
