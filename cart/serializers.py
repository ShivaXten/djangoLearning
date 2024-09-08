# cart/serializers.py

from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'price', 'discounted_price']
