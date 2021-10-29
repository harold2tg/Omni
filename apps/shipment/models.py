#Django
from django.db import models

# Other utilities
from ..otherUtilities.models import Mybaseclass

# Other order
from ..order.models import Order


class Shipment(Mybaseclass, models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    delivery_address = models.CharField(
        max_length=254
    )
    cell_phone_number = models.CharField(
        max_length=16
    )
    city = models.CharField(
        max_length=120
    )
    status = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "Shipments"

    def __str__(self):
        return self.delivery_address
