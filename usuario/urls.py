from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
   # path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
   path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
   # path('validar_login/', views.validar_login, name='validar_login'),
    #path('sair/', views.sair, name='sair'),
]