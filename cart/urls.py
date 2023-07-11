from django.urls import path
from .views import CartView, AddToCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name="cart"),
    path('products/<int:pk>', AddToCartView.as_view(), name="add_to_cart"),
]
