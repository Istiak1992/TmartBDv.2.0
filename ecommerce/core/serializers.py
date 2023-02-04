from rest_framework import serializers
from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = "__all__"

        
class ProductSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()
    prodimg = ProductImageSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


