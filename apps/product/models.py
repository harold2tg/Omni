# Django
from django.db import models

# Other utilities
from ..otherUtilities.models import Mybaseclass


class Products(Mybaseclass, models.Model):
    name = models.CharField(
        max_length=150,
        unique=True
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    stock = models.PositiveSmallIntegerField()
    # is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        db_table = "Products"

    def __str__(self):
        return self.name


