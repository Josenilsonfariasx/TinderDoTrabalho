from hashlib import sha256
from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib import request

from .models import Administrador


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    #senha = sha256 (senha.encode()).hexdigest()
    usuario = Administrador.objects.filter(email = email).filter(senha=senha)

    if (len(usuario) == 0):
        return redirect('/auth/login/?status=1')
    elif(len(usuario)>0):
        request.session['usuario'] = usuario[0].id
        return redirect (f'/auth/home/?status=0')

def home(request):
    status = request.GET.get('status')

    return render (request, 'home.html', {'status':status})


def sair(request):
    pass
