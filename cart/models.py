from django.db import models
from django.conf import settings

# Create your models here.


class Product(models.Model):
    Product = models.ForeignKey("main.Product", on_delete=models.CASCADE)
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    count = models.PositiveSmallIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    price = models.PositiveIntegerField()