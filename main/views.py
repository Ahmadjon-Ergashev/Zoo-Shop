from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, MainCategory
from django.db.models import Q
# Create your views here.

class MainView(ListView):
    model = MainCategory
    template_name = 'home.html'
    
    
class ProductsView(ListView):
    model = Product
    template_name = 'products.html'
    queryset = model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = MainCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category = self.request.GET.get('category', None)
        maincategory = self.request.GET.get('maincategory', None)
        subcategory = self.request.GET.get('subcategory', None)

        if maincategory:
            # return queryset.filter(category__main_category__id=maincategory)
            return queryset.filter(Q(category__main_category__id=maincategory) | Q(category__sub_category__main_category__id=maincategory))
            
        if subcategory:
            return queryset.filter(category__sub_category__id=subcategory)
        if category:
            return queryset.filter(category=category)
        return queryset

class AboutView(TemplateView):
    template_name = 'about.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'