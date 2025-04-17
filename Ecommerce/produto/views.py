from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from . import views
import django.views as View
from django.views.generic import View


class ListaProdutos(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Listar')
class DetalheProduto(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
class AdicionarAoCarrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Adicionar carrinho')
class RemoverDoCarrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')
class Carrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
class Finalizar(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
