# Django
from django.db import models

# Other utilities
from ..otherUtilities.models import Mybaseclass

# Other order
from ..order.models import Order_details


class Payment(Mybaseclass, models.Model):
    """The status field will indicate if the payment provider response is positive"""

    order = models.ForeignKey(
        Order_details,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        default=0
    )

    status = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "Payments"

    def __str__(self):
        return self.pk