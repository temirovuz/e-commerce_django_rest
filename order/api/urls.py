from django.urls import path

from order.api.views import OrderList, OrderAddView

urlpatterns = [
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/add/<int:pk>', OrderAddView.as_view(), name='order-add'),
]