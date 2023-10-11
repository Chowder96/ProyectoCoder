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
        curso = Curso(nombre=request.POST["nombre"].capitalize(), comision=request.POST["comision"])
        curso.save()
        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html")

def crearProfesor(request):
    if request.method == "POST":
        miFormulario = profesorFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor_nuevo = Profesor(nombre=informacion["nombre"].capitalize(), apellido=informacion["apellido"].capitalize(), email=informacion["email"], profesion=informacion["profesion"].capitalize())
            profesor_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        miFormulario = profesorFormulario()
    return render(request, "AppCoder/crearProfesor.html", {"miFormulario": miFormulario})

def crearEstudiante(request):
    if request.method == "POST":
         formulario_estudiante = estudianteFormulario(request.POST)

         if formulario_estudiante.is_valid():
             info_estudiante = formulario_estudiante.cleaned_data
             estudiante_nuevo = Estudiante(nombre=info_estudiante["nombre"].capitalize(), apellido=info_estudiante["apellido"].capitalize(), email=info_estudiante["email"], edad=info_estudiante["edad"])
             estudiante_nuevo.save()
             return render(request, "AppCoder/inicio.html")
    else:
             formulario_estudiante = estudianteFormulario()
    return render(request, "AppCoder/crearEstudiante.html", {"formulario_estudiante": formulario_estudiante})

def crearEntregable(request):
    if request.method == "POST":
        formulario_entregable = entregableFormulario(request.POST)

        if formulario_entregable.is_valid():
            info_entregable = formulario_entregable.cleaned_data
            entregable_nuevo = Entregable(nombre=info_entregable["nombre"].capitalize(), fecha_entrega=info_entregable["fecha_entrega"], estado=info_entregable["estado"])
            entregable_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario_entregable = entregableFormulario()
    return render(request, "AppCoder/crearEntregable.html", {"formulario_entregable": formulario_entregable})

def buscar_profesor(request):
    return render(request, "AppCoder/buscar_profesor.html")

def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

def resultado_profesores(request):
        
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        lista_profesores = Profesor.objects.filter(apellido__icontains=apellido)

        return render(request, "AppCoder/resultado_profesor.html", {'valor':apellido, "lista_profesores": lista_profesores})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return render(request, "AppCoder/buscar_profesor.html", {"respuesta": respuesta})