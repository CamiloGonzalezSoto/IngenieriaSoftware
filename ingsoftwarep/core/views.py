from django.shortcuts import render
from .models import registro_usuario
from .forms import signUpform
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
    return render(request,'core/signUp.html')



def Test(request):
    
    registra= registro_usuario.objects.all()

    datos={
        'registro_usuario':registra
    }

    return render(request,'core/test.html',datos)

def signUp(request):
    data = {
        'form': signUpform()
    }
    if request.method == 'POST': 
        formulario = signUpform(request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"]="Éxito  "

        else:
            data["form"]=formulario  


    return render(request, 'core/signUp.html', data)

    
