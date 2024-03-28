from django.db import models

from base.models import TimeStampedModel
from category.models import Category
from account.models import User
from product.managers import ProductManager


class Color(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Size(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, null=True, blank=True)

    custom = ProductManager()
    objects = models.Manager()

    def __str__(self):
        return self.title


class Images(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.product.title
