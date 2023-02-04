from django.contrib import admin
from .models import Category, Product, Banner, ProductImage

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Banner)
