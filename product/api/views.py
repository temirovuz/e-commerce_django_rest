from rest_framework import generics

from product.api.serializers import ProductSerializer
from product.models import Product


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category').prefetch_related('color', 'size').all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()