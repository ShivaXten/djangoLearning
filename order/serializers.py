from rest_framework import serializers
from .models import OrderItem,Location,Coupon
from products.models import Product
from products.serializers import ProductSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'totalQuantity', 'shippingAddress','coupon_code','paymentMethod']



class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  
    
    class Meta:
        model = OrderItem
        #this will include exclude=['location'] is same as this (field='__all__' -location)
        exclude = ['location','coupon']




# This is the serializer with logic too 
class CouponVerifySerializer(serializers.Serializer):
    coupon_code = serializers.CharField(required=False, allow_blank=True)