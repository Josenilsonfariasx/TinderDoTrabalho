from hashlib import sha256
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'login.html')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256 (senha.encode()).hexdigest()

    return HttpResponse(f'{email} {senha}')

"""    if email == 'fariasx@gmail.com' and senha == 'admin':
        return redirect('/auth/home') 
    else:
        return redirect('/auth/login/?status=1')"""

def home(request):
    return render(request, 'home.html')