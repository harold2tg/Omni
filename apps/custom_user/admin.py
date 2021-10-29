# Django
from django.contrib import admin

# User
from ..custom_user.models import User

admin.site.register(User)
