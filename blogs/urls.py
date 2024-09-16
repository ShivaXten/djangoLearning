from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogReadOnlyModelViewSet

router = DefaultRouter()
router.register('blog_all', BlogReadOnlyModelViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]

