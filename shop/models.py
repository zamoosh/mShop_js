from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    name: models.CharField = models.CharField(max_length=300)
    price: models.IntegerField = models.IntegerField()
    description: models.CharField = models.CharField(max_length=1000)
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture: models.ImageField = models.ImageField(null=True)

    def __str__(self):
        return self.name


User = get_user_model()


class ShoppingCart(models.Model):
    product: models.ManyToManyField = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


class Detail(models.Model):
    product: models.OneToOneField = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
