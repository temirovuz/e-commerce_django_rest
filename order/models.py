
from django.db import models

from base.models import TimeStampedModel
from account.models import User
from product.models import Product


class OrderItem(TimeStampedModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderitem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderitem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} * {self.product.price} = {self.total_price}'

    def calc_price(self):
       return self.quantity * self.product.price

    def save(self, *args, **kwargs):
        self.total_price = self.calc_price()
        return super(OrderItem, self).save(*args, **kwargs)


class Order(TimeStampedModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    orderitem = models.ManyToManyField(OrderItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.total_price}'

    def calc_total(self):
        total = 0
        for orderitem in self.orderitem.objects.all():
            total += orderitem.total_price
        return total

    # def save(self, *args, **kwargs):
    #     self.total_price = self.calc_total()
    #     return super(Order, self).save(*args, **kwargs)
