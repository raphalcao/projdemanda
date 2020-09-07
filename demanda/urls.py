from django.urls import path

from .views import DemandaAPIView, UserAPIView, EnderecoAPIView

urlpatterns = [
    path('demandas/', DemandaAPIView.as_view(), name='demandas'),
    path('users/', UserAPIView.as_view(), name="users"),
    path('enderecos/', EnderecoAPIView.as_view(), name="enderecos"),
]