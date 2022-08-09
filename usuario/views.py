from hashlib import sha256
from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuario.models import usuario


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

    Usuario = usuario.objects.filter(email = email).filter(senha = senha)

    if (len(Usuario) == 0):
        return redirect('/auth/logar/?status=1')
    elif(len(Usuario)>0):
        request.session['Usuario'] = usuario[0].id   
        return redirect ('/auth/home_user/?status=0')

def home_user(request):
    pass