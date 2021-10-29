# Django
from django.urls import path

# Product app
from apps.order.api_orden.view.order_view import (
    OrderListAPIView,
    OrderCreateAPIView,
    OrderUpdateAPIView,
    OrderDestroyAPIView,
    OrderDetailAPIView,
)

from apps.order.api_orden.view.order_items_view import (
    OrderItemsListAPIView,
    OrderItemsCreateAPIView,
    OrderItemsUpdateAPIView,
    OrderItemsDestroyAPIView,
    OrderItemsDetailAPIView,
)

urlpatterns = [
    path('list/', OrderListAPIView.as_view(), name='order_list'),
    path("create/", OrderCreateAPIView.as_view(), name='create_order'),
    path("update/<int:pk>/", OrderUpdateAPIView.as_view(), name='update_order'),
    path("delete/<int:pk>/", OrderDestroyAPIView.as_view(), name='delete_order'),
    path("detail/<int:pk>/", OrderDetailAPIView.as_view(), name='detail_order'),
    path('items_list/', OrderItemsListAPIView.as_view(), name='order_items_list'),
    path('items_list_create/', OrderItemsCreateAPIView.as_view(), name='create_order_items'),
    path("items_list_update/<int:pk>/", OrderItemsUpdateAPIView.as_view(), name='update_order_items'),
    path("items_list_delete/<int:pk>/", OrderItemsDestroyAPIView.as_view(), name='delete_order_items'),
    path("items_list_detail/<int:pk>/", OrderItemsDetailAPIView.as_view(), name='detail_order_items')

]