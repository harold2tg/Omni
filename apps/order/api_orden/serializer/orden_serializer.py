# Rest_framework
from rest_framework import serializers

# product model
from ...models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'user',
            'total'
        ]
