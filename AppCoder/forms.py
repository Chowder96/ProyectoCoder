from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class profesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class estudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()

class cursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()

class entregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_entrega = forms.DateField()
    estado = forms.BooleanField()

class Meta(UserCreationForm):
    model = User
    fields = ['username', 'email', 'password1', 'password2']
