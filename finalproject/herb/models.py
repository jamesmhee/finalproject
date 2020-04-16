from django.db import models
from setuptools.command.upload import upload
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as U


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    quanlity = models.IntegerField()
    price = models.FloatField()

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount = models.IntegerField()
    end_promotion = {
        ('S', 'SALE'),
        ('NS', 'NOTSALE')
    }

class Order(models.Model):
    date = models.DateField(null=True, blank=True)
    delevery_location = models.TextField(blank=True)
    total_price = models.FloatField()
    payment_status = {
        ('AR' ,'Arrived'),
        ('NA' ,'Not_Arrived')
    }
    user_id = models.ForeignKey(U, on_delete=models.CASCADE)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class Payment(models.Model):
    date = models.DateField(null=True, blank=True)
    upload = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order_Product(models.Model):
    unit = models.IntegerField()
    unit_price = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
