from rest_framework import serializers

from category.api.serializers import CategorySerializer
from product.models import Product, Color, Size


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
