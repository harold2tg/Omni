# Rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly

# product
from ...models import Shipment
from apps.shipment.api_shipment.serializer.shipment_serializer import ShipmentSerializer


class ShipmentListAPIView(generics.ListAPIView):
    """This endpoint list all of the available Payment from the database"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    paginate_by = 10
    permission_classes = [IsAuthenticated]


class ShipmentCreateAPIView(generics.CreateAPIView):
    """This endpoint allows for creation of a Payment"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ShipmentUpdateAPIView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific Products by passing in the id of the Payment to update"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ShipmentDestroyAPIView(generics.DestroyAPIView):
    """This endpoint allows for deletion of a specific Payment from the database"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ShipmentDetailAPIView(generics.RetrieveAPIView):
    """This endpoint allows for detail of a specific Products from the database"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

