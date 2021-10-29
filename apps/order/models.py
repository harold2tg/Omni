# Django
from django.db import models
# Products
from ..product.models import Products
# other utilities
from ..otherUtilities.models import Mybaseclass
# User
from ..custom_user.models import User


class Order(Mybaseclass,models.Model):
    """The paid_out field will indicate if the order is fully paid.
    Only when the amount is equal to the total in the order detail is paid_out set to true
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2
    )

    paid_out = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "Order"

    def __str__(self):
        return str(self.pk)


class Order_items(Mybaseclass,models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "Orders_items"

    def __str__(self):
        return str(self.product.name)