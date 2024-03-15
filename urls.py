# ecommerce_app/urls.py
from django.urls import path
from .views import main_category_list, sub_category_list, product_list, product_detail

urlpatterns = [
    # path('main_category', main_category_list, name='main_category_list'),
    path('', main_category_list, name='main_category_list'),
    path('sub-categories/<int:main_category_id>/', sub_category_list, name='sub_category_list'),
    path('products/<int:sub_category_id>/', product_list, name='product_list'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
]
