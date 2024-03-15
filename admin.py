from django.contrib import admin
from .models import MainCategory,SubCategory,Product
# Register your models here.
@admin.register(MainCategory)
class AdminMainCategory(admin.ModelAdmin):
    list_display=['image','name']

@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display=['image','name','main_category']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['name','image','description','price','sub_category']
