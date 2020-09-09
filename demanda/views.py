from rest_framework import generics
from .models import User, Endereco, Demanda
from .serializers import UserSerializer, EnderecoSerializer, DemandaSerializer

"""
from.permissions import ValidaSuperUser

"""

class DemandasAPIView(generics.ListCreateAPIView):
    """
    permission_classes = (
        ValidaSuperUser,
    )
    """
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer


class DemandaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer


class EnderecosAPIView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EnderecoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

