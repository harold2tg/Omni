from rest_framework import serializers

# product model
from ...models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = [
            'order',
            'delivery_address',
            'cell_phone_number',
            'city'
        ]
