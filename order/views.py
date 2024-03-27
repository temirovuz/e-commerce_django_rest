
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import (
    Order,
    OrderItem
)

from .tasks import send_email
from product.models import Product


@login_required(login_url='/accounts/login/')
def order_summary(request):

    order = Order.objects.filter(customer=request.user, ordered=False).annotate(
        order_total_price=Sum('orderitem__total_price')
    ).first()
    context = {
        'order': order
    }

    return render(request, 'order/cart.html', context)




@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        customer=request.user,
        ordered=False
    )

    order_qs = Order.objects.filter(customer=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.orderitem.filter(product__pk=product.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("order:order_summary")
        else:
            order.orderitem.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("order:order_summary")
    else:
        order = Order.objects.create(customer=request.user)
        order.orderitem.add(order_item)
        send_email.delay(order.id)
        messages.info(request, "Item added to your cart")
        return redirect("order:order_summary")


@login_required
def remove_from_cart(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    order = order_item.order_set.all().first()
    if order:
        order.orderitem.remove(order_item)
        order_item.delete()
    return redirect("order:order_summary")


@login_required
def reduce_quantity_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order = Order.objects.filter(
        customer=request.user,
        ordered=False
    ).first()
    if order:
        if order_item:
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitem.remove(order_item)
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("order:order_summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("order:order_summary")
    else:
        # add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("order:order_summary")
