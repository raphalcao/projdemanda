from django.urls import path

from .views import DemandaAPIView, DemandasAPIView, UserAPIView, UsersAPIView, EnderecoAPIView, EnderecosAPIView

urlpatterns = [
    path('demandas/', DemandasAPIView.as_view(), name='demandas'),
    path('demandas/<int:pk>/', DemandaAPIView.as_view(), name='demanda'),
    path('users/', UsersAPIView.as_view(), name="users"),
    path('users/<int:pk>/', UserAPIView.as_view(), name="user"),
    path('enderecos/', EnderecosAPIView.as_view(), name="enderecos"),
    path('enderecos/<int:pk>/', EnderecoAPIView.as_view(), name="endereco"),
]