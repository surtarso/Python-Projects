from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# def index(request):
#     return redirect('/agenda/')

# chamada pelo urls.py
# lista ecentos criados e cria filtros de busca


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Login ou Senha inválidos")
    return redirect('/')


@login_required(login_url='/login/')  # faz a pagina requerer password
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)   # filtra por usuario
    response = {'eventos ': evento}
    # retorna a renderizacao do request com a response no agenda.html
    return render(request, 'agenda.html', response)
