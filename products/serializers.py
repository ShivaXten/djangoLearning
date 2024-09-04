from rest_framework import serializers
from .models import Product, ProductFeatureImage
from reviews.serializers import ReviewSerializer


class ProductFeatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatureImage
        fields = ['image'] 


class ProductSerializer(serializers.ModelSerializer):
    feature_images = ProductFeatureImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    