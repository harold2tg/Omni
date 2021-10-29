# Rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly

# product
from ...models import Payment
from apps.payment.api_payment.serializer.payment_serializer import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """This endpoint list all of the available Payment from the database"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    paginate_by = 10
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(generics.CreateAPIView):
    """This endpoint allows for creation of a Payment"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific Products by passing in the id of the Payment to update"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """This endpoint allows for deletion of a specific Payment from the database"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PaymentDetailAPIView(generics.RetrieveAPIView):
    """This endpoint allows for detail of a specific Products from the database"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

