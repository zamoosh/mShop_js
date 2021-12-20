from django.db import models
from django.contrib.auth import get_user

User = get_user()


class Product(models.Model):
    name: models.CharField = models.CharField()
    price: models.IntegerField = models.IntegerField()
    category: models.CharField = models.CharField(max_length=255)
    description: models.CharField = models.CharField(max_length=1000)


class ShoppingCart(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)


class Detail(models.Model):
    product: models.OneToOneField = models.OneToOneField(Product, on_delete=models.CASCADE)
