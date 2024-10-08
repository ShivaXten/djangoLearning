from django.shortcuts import render
from .models import Product
#imported from the rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer



#This will show that which API of products is Available
@api_view(['GET'])
def productOverview(request):
    product_urls = {
        'Display all products': 'all/',
        'Display by category':'category/<str:category_name>',
        'Display by ID': '<ID>/'

    }

    return Response(product_urls)



#This is to fetch all the products
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()  
    serializer = ProductSerializer(products, many=True)  
    return Response(serializer.data)


#This is to fetch products by ID done by passing the id with request
@api_view(['GET'])
def productDetail(request,pk):
    products = Product.objects.get(id=pk)  
    serializer = ProductSerializer(products, many=False)  
    return Response(serializer.data)


# This is to fetch products category by passing the category name in the response
@api_view(['GET'])
def products_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    if not products.exists():
        return Response({'error': 'No products found for this category'}, status=404)
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

