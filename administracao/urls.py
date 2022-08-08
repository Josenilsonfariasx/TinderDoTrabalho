from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('home/', views.home, name='home'),
    path('sair/', views.sair, name='sair'),
    path('listar_candidatos/', views.listar_candidatos, name='listar_candidatos'),
]
