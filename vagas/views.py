from gc import get_objects
import imp
from importlib.metadata import requires
from multiprocessing import reduction
import re
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from usuario.models import usuario
from .models import Vagas
from .forms import CriarVaga
# Create your views here.

def cadastrar(request):
    return HttpResponse('olaa')

def i_vagas (request,id):
    vaga = Vagas.objects.get(id = id)
    form = CriarVaga
    return render(request, 'info.html',{'vaga': vaga, 'form':form})

def vaga(request, id):
    vaga = get_object_or_404(Vagas, pk=id)
    form = CriarVaga(instance=vaga)
    return render(request,'editar_vaga.html',{'form':form, 'vaga':vaga})

def listar_vagas(request):
    if request.session.get('usuario'):
        vagas = Vagas.objects.all()
        form =CriarVaga
        status = request.GET.get('status')
        return render (request, 'listar.html', {'vagas': vagas, 'form':form, 'status':status})
    else:
        return redirect('/auth/login/?status=2')

def cadastrar_vaga(request):
    if request.method == 'POST':
        form = CriarVaga(request.POST)        
        if form.is_valid():
            form.save()
            return redirect('/vagas/listar_vagas/?status=0')
        else:
            return redirect('/vagas/listar_vagas/?status=1')

def editar_vaga(request, id):
    vaga = get_object_or_404(Vagas, pk=id)
    form = CriarVaga(instance=vaga)
    if request.method == 'POST':
        form = CriarVaga(request.POST, instance=vaga)
        
        if form.is_valid():
            vaga.save()
            return redirect('/vagas/listar_vagas')
        else:
            return render(request, '/vagas/listar_vagas/?status=6')
    else:
        return redirect ('/listar_vagas/?status=5')

def deletar_vaga(request, id):
    vaga = get_object_or_404(Vagas, pk=id)
    vaga.delete()
    return redirect ('/vagas/listar_vagas/?status=6')