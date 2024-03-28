from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):

    def get_categoyr_slug(self, slug):
        qs = super().get_queryset()
        return qs.filter(Q(category__slug=slug))
