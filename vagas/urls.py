from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar_vagas/', views.listar_vagas, name='listar_vagas')

]