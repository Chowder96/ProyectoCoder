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
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
]
