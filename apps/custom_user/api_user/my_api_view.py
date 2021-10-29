# Rest framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Model User
from ..models import User

# Api_user
from .serializer import User_serializer

class User_api_view(APIView):

    def get(self,request):
        users = User.objects.all()
        user_serializer = User_serializer(users,many=True)
        return Response(user_serializer.data)


