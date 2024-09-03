from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Review
from .serializers import ReviewSerializer


# Overview of available review endpoints
@api_view(['GET'])
def reviewsOverview(request):
    review_urls = {
        'List all reviews or create a new review': '/All/',
        'Retrieve, update, or delete a review': '<id>/',
    }
    return Response(review_urls)



# List all reviews or create a new review
@api_view(['GET', 'POST'])
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



# Retrieve, update, or delete a specific review
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        if request.user != review.user:
            return Response({'error': 'You do not have permission to modify this review'}, status=403)
        
        serializer = ReviewSerializer(review, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    
    elif request.method == 'DELETE':
        if request.user != review.user:
            return Response({'error': 'You do not have permission to delete this review'}, status=403)
        
        review.delete()
        return Response(status=204)
