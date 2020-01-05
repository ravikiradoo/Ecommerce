from django.contrib import admin
from .models import Orders,order_item
# Register your models here.
admin.site.register(Orders)
admin.site.register(order_item)

