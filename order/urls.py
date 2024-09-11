from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views 


router = DefaultRouter()

router.register('api',views.OrderModelViewSet,basename='order')
# router.register('pay',views.OrderStatusSerializer,basename='PaymentOfOrder')




urlpatterns = [
    path('', include(router.urls)),
]


