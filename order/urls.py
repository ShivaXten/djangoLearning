from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderModelViewSet, CouponVerifyView 

router = DefaultRouter()

router.register('api', OrderModelViewSet, basename='order')



urlpatterns = [
    path('', include(router.urls)),
    path('verify_coupon/', CouponVerifyView.as_view(), name='verify_coupon'),
]
