from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order, Coupon
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
        return Order.objects.filter(user=self.request.user)
    



# This is to validate the coupon
class CouponVerifyView(APIView):
    def post(self, request):
        serializer = CouponVerifySerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.validated_data
            return Response(response_data)
        return Response(serializer.errors)