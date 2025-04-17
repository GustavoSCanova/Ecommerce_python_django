from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from . import views
import django.views as View

app_name = 'perfil'

urlpatterns =  [
    
    path('', views.Criar.as_view(), name='criar'),
    path('atualizar/', views.Atualzar.as_view(), name='atualizar'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    
    
]