from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Ingrese su Email: ')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta(UserCreationForm):
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__' # Esto incluira todos los campos del modelo avatar en el formulario.