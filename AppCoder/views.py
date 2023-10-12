from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from .forms import *

# Inincio
def inicio(request):
    return render(request, "AppCoder/inicio.html")

# Funciones de CRUD del profesor

# Crear el profesor
#def profe_nuevo(request):
#    profeN = Profesor(nombre="Juan", apellido="Perez", email="q2Z0u@example.com", profesion="Ingeniero")
#    profeN.save()
#    return HttpResponse(f'Hemos guardado al profesor {profeN.nombre}')

# Ver los profesores
def ver_profesores(request):

    todosLosProfesores = Profesor.objects.all()

    return render(request, "AppCoder/ver_profesores.html", {'todosLosProfesores': todosLosProfesores})

#Crear el profesor
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

# Buscar el profesor
def buscar_profesor(request):
    return render(request, "AppCoder/buscar_profesor.html")

def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda
def resultado_profesores(request):
        
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        lista_profesores = Profesor.objects.filter(apellido__icontains=apellido)

        return render(request, "AppCoder/resultado_profesor.html", {'valor':apellido, "lista_profesores": lista_profesores})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return render(request, "AppCoder/buscar_profesor.html", {"respuesta": respuesta})


# Borrar el profesor

def borrar_profesor(request, nombre_profesor):

    borrar_a_profesor = Profesor.objects.get(nombre= nombre_profesor)
    borrar_a_profesor.delete()
    todos = Profesor.objects.all()

    return render(request, "AppCoder/ver_profesores.html", {'todosLosProfesores': todos})

# Funciones de CRUD del curso

# Crear el curso
def curso(request):
    curso_nuevo = Curso(nombre="Python", comision=47765)
    curso_nuevo.save()

    return HttpResponse(f'Hemos guardado el curso {curso_nuevo.nombre}, con el número de comisión: {curso_nuevo.comision}')

def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"].capitalize(), comision=request.POST["comision"])
        curso.save()
        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html")

# Ver los cursos
def ver_cursos(request):

    todosLosCursos = Curso.objects.all()

    return render(request, "AppCoder/ver_cursos.html", {'todosLosCursos': todosLosCursos})


# Borar el curso

def borrar_curso(request, nombre_curso):
    borrar_a_curso = Curso.objects.get(nombre= nombre_curso)
    borrar_a_curso.delete()
    todos = Curso.objects.all()

    return render(request, "AppCoder/ver_cursos.html", {'todosLosCursos': todos})


# Funciones de CRUD del estudiante

# Crear el estudiante
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

# Ver los estudiantes
def ver_estudiantes(request):

    todosLosEstudiantes = Estudiante.objects.all()

    return render(request, "AppCoder/ver_estudiantes.html", {'todosLosEstudiantes': todosLosEstudiantes})


def borrar_estudiante(request, nombre_estudiante):
    borrar_a_estudiante = Estudiante.objects.get(nombre=nombre_estudiante)
    borrar_a_estudiante.delete()

    todos = Estudiante.objects.all()

    return render(request, "AppCoder/ver_estudiantes.html", {'todosLosEstudiantes': todos})


# Buscar el estudiante

def buscar_estudiante(request):
    return render(request, "AppCoder/buscar_estudiante.html")

def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda
def resultado_estudiante(request):
        
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        lista_estudiantes = Estudiante.objects.filter(apellido__icontains=apellido)

        return render(request, "AppCoder/resultado_estudiante.html", {'valor':apellido, "lista_estudiantes": lista_estudiantes})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return render(request, "AppCoder/buscar_estudiante.html", {"respuesta": respuesta})

# Funciones de CRUD del entregable

# Crear el entregable
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

# Ver los entregables
def ver_entregas(request):

    todosLosEntregables = Entregable.objects.all()

    return render(request, "AppCoder/ver_entregas.html", {'todosLosEntregables': todosLosEntregables})


# Borrar entregables

def borrar_entregable(request, nombre_entregable):
    borrar_a_entregable = Entregable.objects.get(nombre=nombre_entregable)
    borrar_a_entregable.delete()

    todos = Entregable.objects.all()

    return render(request, "AppCoder/ver_entregas.html", {'todosLosEntregables': todos})


# Buscar los entregables

def buscar_entregable(request):
    return render(request, "AppCoder/buscar_entregable.html")

def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda
def resultado_entregable(request):
        
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        lista_estudiantes = Entregable.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/resultado_entregable.html", {'valor':nombre, "lista_estudiantes": lista_estudiantes})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["nombre"]}'

    return render(request, "AppCoder/buscar_entregable.html", {"respuesta": respuesta})
