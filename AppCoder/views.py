from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from .forms import *

# Create your views here.

def profe_nuevo(request):
    profeN = Profesor(nombre="Juan", apellido="Perez", email="q2Z0u@example.com", profesion="Ingeniero")
    profeN.save()

    return HttpResponse(f'Hemos guardado al profesor {profeN.nombre}')

def curso(request):
    curso_nuevo = Curso(nombre="Python", comision=47765)
    curso_nuevo.save()

    return HttpResponse(f'Hemos guardado el curso {curso_nuevo.nombre}, con el número de comisión: {curso_nuevo.comision}')

# Context from Code Snippet c:/ProyectoCoder/ProyectoCoder/urls.py:"""

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_cursos(request):
    return render(request, "AppCoder/ver_cursos.html")

def ver_profesores(request):
    return render(request, "AppCoder/ver_profesores.html")

def ver_entregas(request):
    return render(request, "AppCoder/ver_entregas.html")

def ver_estudiantes(request):
    return render(request, "AppCoder/ver_estudiantes.html")

def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        curso.save()
        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html")

def crearProfesor(request):
    if request.method == "POST":
        miFormulario = profesorFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        miFormulario = profesorFormulario()
    return render(request, "AppCoder/crearProfesor.html", {"miFormulario": miFormulario})

def crearEstudiante(request):
    if request.method == "POST":
         miFormulario = estudianteFormulario(request.POST)

         if miFormulario.is_valid():
             informacion = miFormulario.cleaned_data
             estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], edad=informacion["edad"])
             estudiante.save()
             return render(request, "AppCoder/inicio.html")
         else:
             miFormulario = estudianteFormulario()
    return render(request, "AppCoder/crearEstudiante.html", {"miFormulario": miFormulario})