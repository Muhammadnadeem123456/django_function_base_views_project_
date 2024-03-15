# ecommerce_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import MainCategory, SubCategory, Product

def main_category_list(request):
    main_categories = MainCategory.objects.all()
   
    return render(request, 'viewap/main_category_list.html', {'main_categories': main_categories})

def sub_category_list(request, main_category_id):
    sub_categories = SubCategory.objects.filter(main_category_id=main_category_id)
    return render(request, 'viewap/sub_category_list.html', {'sub_categories': sub_categories})

def product_list(request, sub_category_id):
    products = Product.objects.filter(sub_category_id=sub_category_id)
    return render(request, 'viewap/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id) 
    return render(request, 'viewap/product_detail.html', {'product': product})
