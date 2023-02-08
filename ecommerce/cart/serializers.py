from rest_framework import serializers
from .models import *
from core.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="total")
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

    def total(self, cartItem:CartItems):
            return cartItem.quantity * cartItem.product.price


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")
        
        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"] 
        quantity = self.validated_data["quantity"] 
        
        try:
            cartItem = CartItems.objects.get(product_id=product_id, cart_id=cart_id)
            cartItem.quantity += quantity
            cartItem.save()
            
            self.instance = cartItem
            
        
        except:
            
            self.instance = CartItems.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance


    class Meta:
        model = CartItems
        fields = ['id',  'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total


