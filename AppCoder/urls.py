"""ProyectoCoder URL Configuration"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio', inicio, name='Inicio'),

    # Urls para ver
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
    path('buscar_estudiante/', buscar_estudiante, name='buscar_estudiante'),
    path('buscar_entregable/', buscar_entregable, name='buscar_entregable'),

    # Urls de resultados
    path('resultado_profesor/', resultado_profesores, name='resultado_profesor'),
    path('resultado_estudiante/', resultado_estudiante, name='resultado_estudiante'),
    path('resultado_entregable/', resultado_entregable, name='resultado_entregable'),

    # Urls para eliminar
    path('eliminarProfesor/<nombre_profesor>', borrar_profesor, name='eliminarProfesor'),
    path('borrarCurso/<nombre_curso>', borrar_curso, name='eliminarCurso'),
    path('borrarEstudiante/<nombre_estudiante>', borrar_estudiante, name='eliminarEstudiante'),
    path('borrarEntregable/<nombre_entregable>', borrar_entregable, name='eliminarEntregable'),

    # Urls para actualizar
    path('actualizarProfesor/<nombre_profesor>', actualizar_profesor, name='actualizarProfesor'),

    # Urls de listas
    path('estudiantes/listas/', EstudianteLista.as_view(), name='EstudianteLista'),

    # Urls de usuario
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),

    # Url de registro
    path('registro/', create_user, name='registro'),
]
