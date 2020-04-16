from django.contrib import admin
from .models import Product, Promotion, Order_Product, Order, Payment, Image
# Register your models here.

admin.site.register(Product)

admin.site.register(Promotion)

admin.site.register(Order_Product)

admin.site.register(Payment)

admin.site.register(Order)

admin.site.register(Image)