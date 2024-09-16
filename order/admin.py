from django.contrib import admin

# Register your models here.
from .models import OrderItem,Location,Coupon

admin.site.register(OrderItem)

admin.site.register(Location)

admin.site.register(Coupon)

