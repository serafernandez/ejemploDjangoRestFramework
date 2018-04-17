# from users.models import ExchangeUser
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class CView(ListCreateAPIView):

    """
    ListCreateAPIView maneja GetAll y POST 
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class RUDView(RetrieveUpdateDestroyAPIView):

    """
    RetrieveUpdateDestroyAPIView maneja GET, PUT y DELETE
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
