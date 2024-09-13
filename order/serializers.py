from rest_framework import serializers
from .models import Order,Location,Coupon
from products.models import Product
from products.serializers import ProductSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'totalQuantity', 'shippingAddress','coupon_code','paymentMethod']



# class CouponVerifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coupon
#         fields =['Coupon_name']


# class OrderCouponVerifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields =['coupon_code']
    


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  
    
    class Meta:
        model = Order
        #this will include exclude=['location'] is same as this (field='__all__' -location)
        exclude = ['location','coupon']




# This is the serializer with logic too 
class CouponVerifySerializer(serializers.Serializer):
    coupon_code = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        coupon_code = data.get('coupon_code')
        if not coupon_code:
            return {'discount': 0, 'message': 'Coupon code is required.'}
        try:
            # Assuming coupon_code is an exact match for Coupon_name
            coupon = Coupon.objects.get(Coupon_name__iexact=coupon_code)
            return {'discount': coupon.Coupon_Discount, 'message': 'Coupon is valid.'}
        except Coupon.DoesNotExist:
            return {'discount': 0, 'message': 'Coupon code is not valid.'}
