from django.db import models
import uuid
from core.models import Product


# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
         


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items") 
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.product.product_name) + " " + str(self.product.price * self.quantity)
        
    


    
    