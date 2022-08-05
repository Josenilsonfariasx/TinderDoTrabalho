from ast import Return
from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuario.models import usuario
from .models import Vagas
from urllib import request
# Create your views here.

def cadastrar(request):
    return HttpResponse('olaa')

def listar_vagas(request):
    if request.session.get('usuario'):
            vagas = Vagas.objects.all()
            return render (request, 'listar.html', {'vagas': vagas})
    else:
        return redirect('/auth/login/?status=2')
def i_vagas (request,id):
    vaga = Vagas.objects.get(id = id)
    return render(request, 'info.html',{'vaga': vaga})