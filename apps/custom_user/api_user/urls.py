# Django
from django.urls import path

# Api_user
from .my_api_view import User_api_view

urlpatterns = [
    path('list/',User_api_view.as_view(), name='api_usuario')
]