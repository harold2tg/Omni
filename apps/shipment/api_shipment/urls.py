# Django
from django.urls import path

# Product app
from apps.shipment.api_shipment.view.shipment_view import (
    ShipmentListAPIView,
    ShipmentCreateAPIView,
    ShipmentUpdateAPIView,
    ShipmentDestroyAPIView,
    ShipmentDetailAPIView)

urlpatterns = [
    path('list/', ShipmentListAPIView.as_view(), name='shipment_list'),
    path('create/', ShipmentCreateAPIView.as_view(), name='create_shipment'),
    path("update/<int:pk>/", ShipmentUpdateAPIView.as_view(), name='update_shipment'),
    path("delete/<int:pk>/", ShipmentDestroyAPIView.as_view(), name='delete_shipment'),
    path("detail/<int:pk>/", ShipmentDetailAPIView.as_view(), name='detail_shipment')
]