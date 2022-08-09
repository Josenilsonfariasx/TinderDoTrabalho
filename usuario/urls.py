from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
   # path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
   path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
   path('logar/', views.logar, name='logar'),
   path('validar_login/', views.validar_login, name='validar_login'),
   path('home_user/', views.home_user, name='home_user'),
]