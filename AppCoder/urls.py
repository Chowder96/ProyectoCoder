"""ProyectoCoder URL Configuration"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio', inicio),
    path('profesores/', ver_profesores),
    path('cursos/', ver_cursos),
    path('entregas/', ver_entregas),
    path('estudiantes/', ver_estudiantes),
]
