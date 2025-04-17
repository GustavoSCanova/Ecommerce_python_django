from django.urls import path
from django.views import View
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name="pagar"),
    path('FecharPedido/', views.FecharPedido.as_view(), name="fecharpedido"),
    path('Detalhe/', views.Detalhe.as_view(), name="detalhe"),
]
