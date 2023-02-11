from django.db import models

# Create your models here.

class Banner(models.Model):
    banner_name = models.CharField(max_length=100,blank=True,null=True)
    banner = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.banner_name

class Category(models.Model):
    catgory_id = models.AutoField(primary_key=True)
    catgory_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.catgory_name



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=1000,blank=True,null=True)
    core_price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    discount = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    catgory_id = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    

    @property
    def price(self):
        if self.discount > 0:
            price = self.core_price - self.core_price * self.discount / 100
            return price
			
		
	  

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_feature = models.BooleanField(default=False)
    product = models.ForeignKey(Product, related_name='prodimg', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.product_image)


class Order(models.Model):
    order_id = models.CharField(max_length=100,blank=True,null=True)
    product_name = models.CharField(max_length=100,blank=True,null=True)
    quantity = models.IntegerField(default=0)
    core_price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    disscount = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    price = models.CharField(max_length=100,blank=True,null=True)
    sub_total = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)

class Shipping(models.Model):
    order_id = models.CharField(max_length=100,blank=True,null=True)
    customer_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    area = models.CharField(max_length=100,blank=True,null=True)
    thana = models.CharField(max_length=100,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    Note = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.order_id)


  