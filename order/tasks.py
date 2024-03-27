from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

from order.models import Order


@shared_task
def send_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Oloja market: Order number {}'.format(order_id)
    message = 'Good day, {}! You have successfully ordered from Oloja market.\nYour Order number is {}'.format(
        order.customer.username, order.id)
    mailer = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.customer.email])
    return mailer