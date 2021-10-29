# Django
from django.urls import path

# Product app
from apps.product.api_product.view.product_view import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductDetailAPIView)

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='products_list'),
    path('create/', ProductCreateAPIView.as_view(), name='create_product'),
    path("update/<int:pk>/", ProductUpdateAPIView.as_view(), name='update_product'),
    path("delete/<int:pk>/", ProductDestroyAPIView.as_view(), name='delete_product'),
    path("detail/<int:pk>/", ProductDetailAPIView.as_view(), name='detail_product')
]