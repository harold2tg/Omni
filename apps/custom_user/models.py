# django
from django.db import models
from django.contrib.auth.models import AbstractUser

# other utilities
from ..otherUtilities.models import Mybaseclass

class User(Mybaseclass,AbstractUser):

    email = models.EmailField(
        'email_address',
        unique = True,
        error_messages={'Este email ya existe'}
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Ayuda a distinguir los usuarios y a realizar consulta. '
            'El cliente es el principal tipo de usuario '
            )
    )

    def __str__(self):
        return self.username

