from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly

# order
from ...models import Order
from apps.order.api_orden.serializer.orden_serializer import OrderSerializer


class OrderListAPIView(generics.ListAPIView):
    """This endpoint list all of the available order from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    paginate_by = 10
    permission_classes = [IsAdminUser]


class OrderCreateAPIView(generics.CreateAPIView):
    """This endpoint list all of the available order from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class OrderUpdateAPIView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific Products by passing in the id of the Order to update"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class OrderDestroyAPIView(generics.DestroyAPIView):
    """This endpoint allows for deletion of a specific Products from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class OrderDetailAPIView(generics.RetrieveAPIView):
    """This endpoint allows for detail of a specific Products from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
