from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from order.api.permission import OrderPermission
from order.api.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem
from product.models import Product


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, OrderPermission]

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        self.check_object_permissions(self.request, product)
        order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
        orderitem, item_created = OrderItem.objects.get_or_create(product=product, customer=request.user, ordered=False)
        if not item_created:
            orderitem.quantity += 1
            orderitem.save()
        else:
            order.ordered.add(orderitem)

        return Response({'message': 'Ok'}, status=status.HTTP_201_CREATED)
