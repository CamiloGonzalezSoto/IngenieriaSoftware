from django import forms
from django.forms import ModelForm
from .models import registro_usuario


class signUpform(ModelForm):

    class Meta:
        model = registro_usuario
        fields = '__all__'