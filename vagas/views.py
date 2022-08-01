from ast import Return
from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cadastrar(request):
    return HttpResponse('olaa')

def listar_vagas(request):
    return render (request, 'listar.html')