from django.urls import path
from .views import index, ingresoSalida, mandatos, signInDonadores, signInFuncionarios,signUp


urlpatterns = [
    path('',index, name ='index'),
    path('mandatos',mandatos, name='mandatos'),
    path('signInDonadores',signInDonadores, name='signInDonadores'),
    path('signInFuncionarios',signInFuncionarios, name='signInFuncionarios'),
    path('signUp',signUp, name='signUp'),
    path('ingresoSalida',ingresoSalida, name='ingresoSalida'),
]