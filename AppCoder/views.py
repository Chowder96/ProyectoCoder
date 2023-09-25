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
    return HttpResponse("Hola, esta es la vista de inicio!")

def ver_cursos(request):
    return HttpResponse("Hola, esta es la vista de cursos!")

def ver_profesores(request):
    return HttpResponse("Hola, esta es la vista de profesores!")

def ver_entregas(request):
    return HttpResponse("Hola, esta es la vista de entregas!")

def ver_estudiantes(request):
    return HttpResponse("Hola, esta es la vista de estudiantes!")

