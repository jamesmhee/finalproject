from django.db import models
from setuptools.command.upload import upload

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    address = models.TextField()
    province = models.TextField()

class Order(models.Model):
    date = models.DateField(null=True, blank=True)
    delevery_location = models.TextField(blank=true)
    total_price = models.FloatField()
    payment_status = {
        ('AR' ,'Arrived'),
        ('NA' ,'Not_Arrived')
    }
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    promotion_id = models.ForeignKey(promotion, on_delete=models.CASCADE)

class Payment(models.Model):
    date = models.DateField(null=True, blank=True)
    upload = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order_Product(models.Model):
    unit = models.IntegerField(max_length=10)
    unit_price = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    quanlity = models.IntegerField(max_length=10)
    price = models.FloatField()

class Image(models.Model):
    image = models.ImageField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount = models.IntegerField(max_length=10)
    end_promotion = {
        ('S', 'SALE'),
        ('NS', 'NOTSALE')
    }
