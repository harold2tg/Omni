# Rest_framework
from rest_framework import serializers

# product model
from ...models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'order',
            'amount',
            'status'
        ]
