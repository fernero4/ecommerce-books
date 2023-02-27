from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.


def All_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def Categories(request):
    return {'categories': Category.objects.all()}


def Product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/details.html', {'product': product})
