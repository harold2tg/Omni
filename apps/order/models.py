# Django
from django.db import models
# Products
from ..product.models import Product
# other utilities
from ..otherUtilities.models import Mybaseclass
# User
from ..custom_user.models import User
# Payments
from ..payment.models import Payment


class Order(Mybaseclass,models.Model):
    """The paid_out field will indicate if the order is fully paid.
    Only when the amount is equal to the total in the order detail is paid_out set to true
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    total = models.DecimalField()

    paid_out = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "Order"

    def __str__(self):
        return self.pk


class Order_items(Mybaseclass,models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        db_table = "Orders"

    def __str__(self):
        return self.pk