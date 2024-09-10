from rest_framework import serializers
from .models import Order
from products.models import Product
from products.serializers import ProductSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'totalQuantity', 'shippingAddress', 'paymentMethod']
    


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  
    
    class Meta:
        model = Order
        fields = '__all__'
