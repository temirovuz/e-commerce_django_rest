from django.db.models import F


def inc_or_dec(obj, num,is_inc):
    if is_inc:
        obj.quantity = F('quantity') + num
        obj.save()
    else:
        obj.quantity = F('quantity') - num
        obj.save()