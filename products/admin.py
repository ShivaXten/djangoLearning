from django.contrib import admin
from .models import Product, ProductFeatureImage

class ProductFeatureImageInline(admin.TabularInline):
    model = ProductFeatureImage
    extra = 1  # Number of empty forms to display initially

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'availability_status')
    inlines = [ProductFeatureImageInline]

@admin.register(ProductFeatureImage)
class ProductFeatureImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')