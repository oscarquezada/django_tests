from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('productos/', views.listar_productos, name='listar_productos'),  # <-- Agregado
    path('vista-html/',  views.vista_html, name='vista_html'),
    path('vista-contexto/',  views.vista_contexto, name='vista_contexto'),
    path('vista-json/',  views.vista_json, name='vista_json'),
    path('vista-redirect/',  views.vista_redirect, name='vista_redirect'),
]
