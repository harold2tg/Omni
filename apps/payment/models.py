# Django
from django.db import models

# Other utilities
from ..otherUtilities.models import Mybaseclass

# Other order
from apps.order.models import Order


class Payment(Mybaseclass, models.Model):
    """The status field will indicate if the payment provider response is positive"""

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    status = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "Payments"

    # def __str__(self):
    #     return str(self.orden)
