from django.db import models


class Mybaseclass(models.Model):
    created = models.DateTimeField(
        'created_at',
        auto_now_add=True
        )
    modified = models.DateTimeField(
        'modified_at',
        auto_now=True
    )

    class Meta:
        abstract = True
