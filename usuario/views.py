from hashlib import sha256
import re
from sqlite3 import adapt
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuario.models import usuario
from vagas.forms import forms
from vagas.models import Vagas

def cadastrar(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})

def validar_cadastro(request):
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    nome = request.POST.get('nome')

    Usuario = usuario.objects.filter(email = email)

    if len(email.strip()) == 0 or len(senha.strip()) == 0 or len(nome.strip()) == 0 :
        return redirect ('/auth/cadastrar/?status=1')
    
    elif len(senha) < 8:
        return redirect ('/auth/cadastrar/?status=2')
    
    if len(Usuario) > 0:
        return redirect ('/auth/cadastrar/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest
        Usuario = usuario(nome = nome, email=email, senha = senha)
        Usuario.save()

        return redirect ('/auth/logar/?status=0')
    except:
        return redirect ('/auth/cadastrar/?status=4')

def logar(request):
    status = request.GET.get('status')
    return render(request, 'logar.html', {'status':status})

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuarios = usuario.objects.filter(email = email).filter(senha = senha)
    
    if (len(usuarios) == 0 and len(senha) == 0):
        return redirect('/auth/logar/?status=1')
    else:
        request.session['candidatos'] = usuarios[0].email
        return redirect('/auth/home_user/?status=0')

def home_user(request):
    usuarios = usuario.objects.get(email = request.session.get('candidatos'))
    user = request.session['candidatos'] 
    return render(request, 'home_user.html', {'user':user, 'usuarios':usuarios})

def listar(request):
    vaga = Vagas.objects.all()
    status = request.GET.get('status')
    usuarios = usuario.objects.all()
    return render (request, 'listagem.html',{'vagas':vaga,'usuarios':usuarios ,'status':status})
    

def entrar_vaga(request, id):
    vagas = Vagas.objects.get(id = id)
    status = request.GET.get('status')
    return render(request, 'vaga_entrar.html',{'vagas':vagas, 'status':status})

def perfil(request):
    usuarios = usuario.objects.get(email = request.session.get('candidatos'))
    return render(request, 'perfil.html', {'usuarios':usuarios})