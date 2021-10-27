# Django
from django.db import models

# Other utilities
from ..otherUtilities.models import Mybaseclass


class Product(Mybaseclass, models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.DecimalField()
    stock = models.PositiveSmall()
    # is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        db_table = "Products"

    def __str__(self):
        return self.name


