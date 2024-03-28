from django.urls import path

from category.api.views import CategoryListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list')
]