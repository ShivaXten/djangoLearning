from django.urls import path
from . import views 


urlpatterns = [

path('',views.productOverview, name="productOverview"),
path('all/',views.productList, name="productList"),
path('<str:pk>',views.productDetail, name="productDetail"),

]
