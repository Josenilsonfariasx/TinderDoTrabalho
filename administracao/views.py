from hashlib import sha256
from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib import request
from administracao.models import Administrador
from vagas.forms import CriarVaga
from vagas.models import Vagas
from usuario.models import usuario

def login(request):

    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    
    usuario = Administrador.objects.filter(email = email).filter(senha=senha)

    if (len(usuario) == 0):
        return redirect('/auth/login/?status=1')
    elif(len(usuario)>0):
        request.session['usuario'] = usuario[0].id   
        return redirect (f'/auth/home/?status=0')
    

def sair(request):
    request.session.flush()
    return redirect ('/auth/login/')

def home(request):
    
    status = request.GET.get('status')
    if request.session.get('usuario'):
        administrador = Administrador.objects.get(id = request.session['usuario'])
        return render(request,'home.html',{'status':status})
    else:
        return redirect ('/auth/login/?status=2')

def listar_candidatos(request):
    candidatos = usuario.objects.all()
    return render (request, 'listar_candidatos.html', {'candidatos':candidatos})
