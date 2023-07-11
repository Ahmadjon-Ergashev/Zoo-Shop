from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Product
# Create your views here.

class CartView(ListView):
    model = Product
    template_name = 'cart.html'

class AddToCartView(CreateView):
    model = Product
    template_name = 'product_detail.html'
