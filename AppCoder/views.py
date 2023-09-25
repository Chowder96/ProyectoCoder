from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor, Curso

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

