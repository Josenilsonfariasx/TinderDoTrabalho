from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar_vagas/', views.listar_vagas, name='listar_vagas'),
    path('i_vagas/<int:id>', views.i_vagas, name='i_vagas'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga')
]