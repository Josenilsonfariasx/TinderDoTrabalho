from hashlib import sha256
from django.shortcuts import render
from django.http import HttpResponse


def cadastrar(request):
    return render(request, 'cadastro.html')



def validar_cadastro(request):
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    nome = request.POST.get('nome')

   # senha = sha256 (senha.encode()).hexdigest()

    return HttpResponse(f'{nome} {email} {senha}')
