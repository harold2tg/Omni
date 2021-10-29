# Rest_framework
from rest_framework import serializers

# product model
from ...models import Order_items


class OrderItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_items
        fields = [
            'order',
            'product',
            'quantity'
        ]
