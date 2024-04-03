from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'order']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product_count'] = instance.products.count()
        return data

