from django.db import models
from django.urls import reverse

# Create your models here.

class Units(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title

class MainCategory(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/MainCataegory/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    def __str__(self) -> str:
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True, related_name='SubCategory')
    photo = models.ImageField(upload_to='images/SubCataegory/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='MainCategory')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='Category')
    photo = models.ImageField(upload_to='images/Cataegory/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/Products/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    weight = models.PositiveSmallIntegerField()
    raiting = models.FloatField()
    unit = models.ForeignKey(to=Units, default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True)
    sold_count = models.PositiveSmallIntegerField(null=True)
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

class Tags(models.Model):
    title = models.CharField(max_length=30)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.title
