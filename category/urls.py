from django.urls import path

from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
]
