from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Review, Product
from .serializers import ReviewSerializer


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
    
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user) 
        return Response(serializer.data, status=201)
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
    
    review.delete()
    return Response(status=204)

