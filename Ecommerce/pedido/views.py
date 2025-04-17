from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from . import views
import django.views as View
from django.views.generic import View

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')
    
class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
    
