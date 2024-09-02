from django.shortcuts import render
from .models import Product
#imported from the rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer



#This will show that which API of products is Available
@api_view(['GET'])
def productOverview(request):
    product_urls={
        "list":"/productList/",
    }

    return Response("product_urls")



#This is to fetch all the products
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()  
    serializer = ProductSerializer(products, many=True)  
    return Response(serializer.data)


