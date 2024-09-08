# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_overview, name='cart-overview'),
    path('current/', views.cart_list, name='cart-list'),
    path('<int:pk>/', views.cart_detail, name='cart-detail'),
    path('addProduct/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('update/<int:pk>/', views.update_cart_item, name='update-cart-item'),
    path('delete/<int:pk>/', views.delete_cart_item, name='delete-cart-item'),
]
