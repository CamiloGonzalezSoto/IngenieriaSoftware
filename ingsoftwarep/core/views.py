from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'core/index.html')


def ingresoSalida(request):
    return render(request,'core/ingresoSalida.html')

def mandatos(request):
    return render(request,'core/mandatos.html')

def signInDonadores(request):
    return render(request,'core/signInDonadores.html')

def signInFuncionarios(request):
    return render(request,'core/signInFuncionarios.html')

def signUp(request):
    return render(request,'core/sign.html')