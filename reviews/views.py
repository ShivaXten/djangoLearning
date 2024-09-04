from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Review, Product
from .serializers import ReviewSerializer
from .utils import update_product_rating


# Overview of available review endpoints
@api_view(['GET'])
def reviewsOverview(request):
    review_urls = {
        'List all reviews': 'all/',
        'Create a review for a specific product': 'create/<product_id>/',
        'Update a review': 'update/<id>/',
        'Delete a review': 'delete/<id>/',
    }
    return Response(review_urls)


# This is to list all the listViews available 
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# Create a new review for a specific product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    data = request.data.copy()
    data['product'] = product_id  
    
    # Check if the user has already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    
    if existing_review:
        # Update the existing review
        serializer = ReviewSerializer(existing_review, data=data, partial=True)
    else:
        # Create a new review
        serializer = ReviewSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)
        # Update the product rating after saving the review
        update_product_rating(product)
        return Response(serializer.data, status=200 if existing_review else 201)
    return Response(serializer.errors, status=400)


# This is to update the review in any case PATCH 
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)
    
    if request.user != review.user:
        return Response({'error': 'You do not have permission to modify this review'}, status=403)
    
    serializer = ReviewSerializer(review, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        # Update the product rating after updating the review
        update_product_rating(review.product)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



# This is to delete the review if it belongs to current user  
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)

    if request.user != review.user:
        return Response({'error': 'You do not have permission to delete this review'}, status=403)

    # Capture review details before deletion
    review_data = {
        'id': review.id,
        'rating': review.rating,
        'comment': review.comment,
        'date': review.date,
    }

    product = review.product
    review.delete()

    # Update the product rating after deleting the review
    update_product_rating(product)
    
    # Return the deleted review information in the response
    return Response({'message': 'Review deleted', 'review': review_data}, status=200)

