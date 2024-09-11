from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderCreateSerializer, OrderDetailSerializer




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
    



# class OrderStatusSerializer(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         if self.action in ['create', 'update']:
#             return OrderStatusSerializer
#         return OrderDetailSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def get_queryset(self):
        return Order.objects.filter(user=self.request.user)





# class OrderReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         return OrderDetailSerializer

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)
