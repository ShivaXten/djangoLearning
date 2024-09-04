from django.urls import path
from . import views


urlpatterns = [
    path('', views.productOverview, name="productOverview"),
    path('all/', views.productList, name="productList"),
    path('category/<str:category_name>/', views.products_by_category, name='products-by-category'),
    path('<int:pk>/', views.productDetail, name="productDetail"),
]
