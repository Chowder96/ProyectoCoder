"""ProyectoCoder URL Configuration"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio', inicio, name='Inicio'),
    path('profesores/', ver_profesores, name='VerProfesores'),
    path('cursos/', ver_cursos, name='VerCursos'),
    path('entregas/', ver_entregas, name='VerEntregas'),
    path('estudiantes/', ver_estudiantes, name='VerEstudiantes'),

    # Urls para crear
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('crearProfesor/', crearProfesor, name='crearProfesor'),
    path('crearEstudiante/', crearEstudiante, name='crearEstudiante'),
    path('crearEntregable/', crearEntregable, name='crearEntregable'),

    # Urls para buscar
    path('buscar_profesor/', buscar_profesor, name='buscar_profesor'),
    path('buscar/', buscar),

    # Urls de resultados
    path('resultado_profesor/', resultado_profesores, name='resultado_profesor'),
]
