from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'seller'),
        (3, 'custumer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    phone_number = models.CharField(max_length=13)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name='users', null=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='users', null=True)

    def __str__(self):
        return self.username

    @property
    def is_seller(self):
        return self.user_type == 2

    @property
    def is_customer(self):
        return self.user_type == 3


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    text = models.CharField(max_length=225)

    def __str__(self):
        return self.text[:10]