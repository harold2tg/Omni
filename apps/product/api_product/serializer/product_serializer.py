# Rest_framework
from rest_framework import serializers

# product model
from ...models import Products


class Product_serializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'name',
            'price',
            'stock'
        ]
