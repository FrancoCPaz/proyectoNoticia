from django import forms
from .models import Genero, Noticia

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ["genero",]
        labels = {'genero':'Genero',}


class noticiaForm(forms.ModelForm):
    nombre = forms.CharField(required=True,  max_length=50)
    descripcion = forms.CharField(max_length=100, required=True)#,widget=forms.Textarea)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Noticia
        fields= ['nombre', 'descripcion','imagen']


