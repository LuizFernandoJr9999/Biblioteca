from django import forms 
from .models import Livros , Categoria 
from django.db import models
from datetime import date 

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
        #fields = ('nome', 'autor', 'co_autor', 'data_cadastro', 'emprestado', 'categoria')

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.fields['usuario'].widget = forms.HiddenInput() 

'''class CadastroLivro(forms.Form):
    nome = forms.CharField(max_length = 100)
    autor = forms.CharField(max_length = 30)
    co_autor = forms.CharField(max_length = 30 )
    data_cadastro = forms.DateField()
    emprestado = forms.BooleanField()
'''

class CategoriaLivro(forms.Form):
    nome = forms.CharField(max_length=30)
    #descricao = forms.CharField(max_length=60)
    descricao = forms.CharField(max_length=60)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea()