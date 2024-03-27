from django.contrib import admin

from product.models import Product, Images, Color, Size

# Register your models here.
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)