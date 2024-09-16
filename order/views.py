from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import OrderItem, Coupon
from .serializers import OrderCreateSerializer, OrderDetailSerializer,CouponVerifySerializer
# ,OrderCouponVerifySerializer
from rest_framework.views import APIView




class OrderModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return OrderCreateSerializer
        return OrderDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user)
    



# This is to validate the coupon
class CouponVerifyView(APIView):
    def post(self, request):
        serializer = CouponVerifySerializer(data=request.data)
        
        if serializer.is_valid():
            coupon_code = serializer.validated_data.get('coupon_code')
            
            if not coupon_code:
                return Response({'discount': 0, 'message': 'Coupon code is required.'}, status=400)
            
            try:
                # Assuming coupon_code is an exact match for Coupon_name
                coupon = Coupon.objects.get(Coupon_name__iexact=coupon_code)
                return Response({'discount': coupon.Coupon_Discount, 'message': 'Coupon is valid.'})
            except Coupon.DoesNotExist:
                return Response({'discount': 0, 'message': 'Coupon code is not valid.'}, status=400)
        
        return Response(serializer.errors, status=400)