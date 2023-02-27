from .models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.


def Categories(request):
    return {'categories': Category.objects.all()}


def All_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def Product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/product_details.html', {'product': product})


def Category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
