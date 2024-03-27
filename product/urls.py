from django.urls import path

from .views import HomeView, ProductListView

app_name = 'product'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
]