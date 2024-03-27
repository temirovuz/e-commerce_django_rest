from order.models import OrderItem


def order_count(request):
    if request.user.is_authenticated:
        order_count = OrderItem.objects.filter(customer=request.user, ordered=False).count()
        return {'order_count': order_count}
    return {'order_count': 0}
