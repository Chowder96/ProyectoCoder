from django import forms

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