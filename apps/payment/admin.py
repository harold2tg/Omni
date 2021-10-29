# Django
from django.contrib import admin

# User
from ..payment.models import Payment

admin.site.register(Payment)
