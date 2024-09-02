from django.urls import path
from . import views 


urlpatterns = [

path('',views.productOverview, name="productOverview"),
path('productList/',views.productList, name="productList"),

]
