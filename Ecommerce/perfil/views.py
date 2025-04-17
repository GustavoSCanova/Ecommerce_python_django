from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
import django.views as View
from django.views.generic import View

class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar')
    
class Atualzar(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')
    
    
class Login(View):
     def get(self, *args, **kwargs):
        return HttpResponse('Login')
    
class Logout(View):
     def get(self, *args, **kwargs):
        return HttpResponse('Logout')