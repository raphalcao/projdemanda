from django.contrib import admin

from .models import User, Endereco, Demanda


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'endereco', 'anunciante', 'finalizado']


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cep', 'endereco', 'numero', 'complemento', 'cidade', 'estado', 'usuario']


admin.site.register(User)
