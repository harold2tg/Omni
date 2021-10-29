# Django
from django.contrib import admin

# User
from ..order.models import Order,Order_items

admin.site.register(Order)
admin.site.register(Order_items)

