
from django.views.generic import ListView

from .models import Category


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/category_list.html'
