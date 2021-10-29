from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly

# order
from ...models import Order_items
from apps.order.api_orden.serializer.orden_items_serializer import OrderItemsSerializer


class OrderItemsListAPIView(generics.ListAPIView):
    """This endpoint list all of the available order_items from the database"""
    queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer
    paginate_by = 10
    permission_classes = [IsAdminUser]


class OrderItemsCreateAPIView(generics.CreateAPIView):
    """This endpoint list all of the available order from the database"""
    queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [IsAuthenticated]


class OrderItemsUpdateAPIView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific Products by passing in the id of the Order to update"""
    queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [IsAdminUser]


class OrderItemsDestroyAPIView(generics.DestroyAPIView):
    """This endpoint allows for deletion of a specific Products from the database"""
    queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [IsAdminUser]


class OrderItemsDetailAPIView(generics.RetrieveAPIView):
    """This endpoint allows for detail of a specific Products from the database"""
    queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [IsAuthenticated]
