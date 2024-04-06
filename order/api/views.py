from django.db.models import F
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from order.api.permission import OrderPermission, OrderItemAuthorPermission
from order.api.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem
from product.models import Product


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderAddView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, OrderPermission]

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        self.check_object_permissions(self.request, product)
        if product.quantity <= 0:
            return Response({"message": "product qolmadi"}, status=status.HTTP_200_OK)
        order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
        orderitem, item_created = OrderItem.objects.get_or_create(product=product, customer=request.user, ordered=False)
        if not item_created:
            orderitem.quantity = F('quantity') + 1
            product.quantity = F('quantity') - 1
        else:
            order.ordered.add(orderitem)
            product.quantity = F('quantity') - 1

        return Response({'message': 'Ok'}, status=status.HTTP_201_CREATED)


class RemoveOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated, OrderItemAuthorPermission]

    def post(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        order = Order.objects.filter(orderitem=orderitem, ordered=False).first()
        self.check_object_permissions(self.request, orderitem)
        orderitem.product.quantity + F('orderitem.quantity')
        order.orderitem.remove(orderitem)
        orderitem.delete()
        return Response({'message': 'ok'}, status=status.HTTP_204_NO_CONTENT)


class OrderItemIncrementApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, OrderItemAuthorPermission]

    def post(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        self.check_object_permissions(self.request, orderitem)
        if orderitem.product.quantity <= 0:
            return Response({"message": "product qolmadi"}, status=status.HTTP_200_OK)
        orderitem.quantity = F('quantity') + 1
        orderitem.save()
        orderitem.product.quantity = F('quantity') - 1
        orderitem.product.save()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)


class OrderItemDecrementApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, OrderItemAuthorPermission]

    def post(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        self.check_object_permissions(self.request, orderitem)
        if orderitem.quantity == 1:
            orderitem.product.quantity = F('quantity') + 1
            orderitem.delete()
            return Response({"message": "Order delete"}, status=status.HTTP_204_NO_CONTENT)
        orderitem.quantity = F('quantity') + 1
        orderitem.save()
        orderitem.product.quantity = F('quantity') + 1
        orderitem.product.save()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
