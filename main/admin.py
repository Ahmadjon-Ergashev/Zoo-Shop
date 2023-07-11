from django.contrib import admin
from .models import Product, Units, MainCategory, SubCategory, Category, Tags

# Register your models here.

admin.site.register(Product)
admin.site.register(Units)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Tags)
