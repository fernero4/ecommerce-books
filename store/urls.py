
from django.urls import path, include
from . import views

app_name = 'store'


urlpatterns = [
    path('', views.All_products, name='All_products'),
    path('item/<slug:slug>', views.Product_detail, name='Product_detail'),

]
