from django.contrib import admin

# Register your models here.
from .models import Order,Location,Coupon

admin.site.register(Order)

admin.site.register(Location)

admin.site.register(Coupon)

