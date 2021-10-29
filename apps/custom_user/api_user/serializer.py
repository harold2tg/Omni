# Rest framework
from rest_framework import serializers

# Model User
from ..models import User

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'groups', 'user_permissions', 'is_superuser']
