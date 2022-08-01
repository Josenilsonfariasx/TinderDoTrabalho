from ast import Return
from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vagas
# Create your views here.

def cadastrar(request):
    return HttpResponse('olaa')

def listar_vagas(request):
    vagas = Vagas.objects.all()
    return render (request, 'listar.html', {'vagas': vagas})