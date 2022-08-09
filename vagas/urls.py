from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar_vagas/', views.listar_vagas, name='listar_vagas'),
    path('i_vagas/<int:id>', views.i_vagas, name='i_vagas'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('vagaEdit/<int:id>', views.vaga, name="edit_vagas"),
    path('vaga_delete/<int:id>', views.deletar_vaga, name="delete_vagas"),
    path('editar_vagas/<int:id>', views.editar_vaga, name="editar_vagas"),
]