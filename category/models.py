from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

from base.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.IntegerField(default=0)

    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sub_category_list', kwargs={'slug': self.slug})
