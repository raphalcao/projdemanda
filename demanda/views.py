from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Endereco, Demanda
from .serializers import UserSerializer, EnderecoSerializer, DemandaSerializer


class DemandaAPIView(APIView):
    """
    Api de Demanda
    """

    def get(self, request):
        demandas = Demanda.objects.all()
        serializer = DemandaSerializer(demandas, many=True)
        return Response(serializer.data)


class EnderecoAPIView(APIView):
    """
    Api de Endereço
    """
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)


class UserAPIView(APIView):
    """
    Api de Usuarios
    """
    def get(self, request):
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)