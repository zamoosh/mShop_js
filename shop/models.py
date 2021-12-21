from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=300)


class Product(models.Model):
    name: models.CharField = models.CharField(max_length=300)
    price: models.IntegerField = models.IntegerField()
    description: models.CharField = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + self.product


class Detail(models.Model):
    product: models.OneToOneField = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
