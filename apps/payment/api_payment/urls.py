# Django
from django.urls import path

# Product app
from apps.payment.api_payment.view.payment_view import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentUpdateAPIView,
    PaymentDestroyAPIView,
    PaymentDetailAPIView)

urlpatterns = [
    path('list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='create_payment'),
    path("update/<int:pk>/", PaymentUpdateAPIView.as_view(), name='update_payment'),
    path("delete/<int:pk>/", PaymentDestroyAPIView.as_view(), name='delete_payment'),
    path("detail/<int:pk>/", PaymentDetailAPIView.as_view(), name='detail_payment')
]