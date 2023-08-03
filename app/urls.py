from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio" ),

    path('cliente/', cliente , name="cliente"),
    path('ipa/', ipa, name="ipa"),
    path('rubia/', rubia, name="rubia"),
    path('form_ipa/', formIpa, name="form_ipa"),
    path('form_ipa2/', formIpa2, name="form_ipa2"),
    path('buscar_ipa/', buscarIpa, name="buscar_ipa"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar_rubia/', buscarRubia, name="buscar_rubia"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
    path('buscar4/', buscar4, name="buscar4"),
    path('form_rubia/', formRubia, name="form_rubia"),
    path('form_rubia2/', formRubia2, name="form_rubia2"),
    path('form_cliente/', formCliente, name="form_cliente"),
    path('form_cliente2/', formCliente2, name="form_cliente2"),


]  