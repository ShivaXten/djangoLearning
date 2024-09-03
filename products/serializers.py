from rest_framework import serializers
from .models import Product
from reviews.serializers import ReviewSerializer

class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product
        fields = '__all__'
    reviews = ReviewSerializer(many=True, read_only=True)




    