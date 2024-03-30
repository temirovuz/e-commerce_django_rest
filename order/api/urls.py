from django.urls import path

from order.api.views import OrderList, OrderAddView, RemoveOrderView

urlpatterns = [
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/add/<int:pk>', OrderAddView.as_view(), name='order-add'),
    path('order/remove/<int:pk>', RemoveOrderView.as_view(), name='order-remove'),
]