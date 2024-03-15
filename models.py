# ecommerce_app/models.py
from django.db import models

class MainCategory(models.Model):
    image = models.ImageField(upload_to='MainCategory_images/')
    name = models.CharField(max_length=100)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='SubCategory_images/')
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
