from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category
from product.models import Product


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/category_list.html'