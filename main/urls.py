from django.urls import path
from .views import MainView, ProductsView, AboutView, ProductDetailView

urlpatterns = [
    path('',  MainView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('about/', AboutView.as_view(), name='about'),
]
