from django.urls import path

from category.api.views import CategoryListView
from product.api.views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='category-list')
]
