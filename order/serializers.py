from rest_framework import serializers
from .models import Order,Location
from products.models import Product
from products.serializers import ProductSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'totalQuantity', 'shippingAddress','coupon_code','paymentMethod']



# class OrderStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['product','orderStatus']
    


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  
    
    class Meta:
        model = Order
        #this will include exclude=['location'] is same as this (field='__all__' -location)
        exclude = ['location','coupon']
