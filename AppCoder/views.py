# Imports

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from AppCoder.models import *
from AppCoder.forms import UserCreationForm, UserEditForm, AvatarFormulario
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
@login_required
def ver_profesores(request):

    todosLosProfesores = Profesor.objects.all()

    return render(request, "AppCoder/ver_profesores.html", {'todosLosProfesores': todosLosProfesores})

#Crear el profesor

@login_required
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

@login_required
def buscar_profesor(request):
    return render(request, "AppCoder/buscar_profesor.html")

def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda

@login_required
def resultado_profesores(request):
        
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        lista_profesores = Profesor.objects.filter(apellido__icontains=apellido)

        return render(request, "AppCoder/resultado_profesor.html", {'valor':apellido, "lista_profesores": lista_profesores})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return render(request, "AppCoder/buscar_profesor.html", {"respuesta": respuesta})


# Borrar el profesor

@login_required
def borrar_profesor(request, nombre_profesor):

    borrar_a_profesor = Profesor.objects.get(nombre= nombre_profesor)
    borrar_a_profesor.delete()
    todos = Profesor.objects.all()

    return render(request, "AppCoder/ver_profesores.html", {'todosLosProfesores': todos})


@login_required
def actualizar_profesor(request, nombre_profesor):

    profesor_escogido = Profesor.objects.get(nombre= nombre_profesor)
    
    if request.method == "POST":
        miFormulario = profesorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            profesor_escogido.nombre = informacion["nombre"]
            profesor_escogido.apellido = informacion["apellido"]
            profesor_escogido.email = informacion["email"]
            profesor_escogido.profesion = informacion["profesion"]

            profesor_escogido.save()

        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = profesorFormulario(initial={"nombre":profesor_escogido.nombre, "apellido":profesor_escogido.apellido, "email":profesor_escogido.email, "profesion":profesor_escogido.profesion})

        return render(request, "AppCoder/actualizar_profesor.html", {"miFormulario": miFormulario, "profesor":profesor_escogido})


# Funciones de CRUD del curso

# Crear el curso
@login_required
def curso(request):
    curso_nuevo = Curso(nombre="Python", comision=47765)
    curso_nuevo.save()

    return HttpResponse(f'Hemos guardado el curso {curso_nuevo.nombre}, con el número de comisión: {curso_nuevo.comision}')

@login_required
def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"].capitalize(), comision=request.POST["comision"])
        curso.save()
        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html")

# Ver los cursos
@login_required
def ver_cursos(request):

    todosLosCursos = Curso.objects.all()

    return render(request, "AppCoder/ver_cursos.html", {'todosLosCursos': todosLosCursos})


# Borar el curso

@login_required
def borrar_curso(request, nombre_curso):
    borrar_a_curso = Curso.objects.get(nombre= nombre_curso)
    borrar_a_curso.delete()
    todos = Curso.objects.all()

    return render(request, "AppCoder/ver_cursos.html", {'todosLosCursos': todos})


# Funciones de CRUD del estudiante

# Crear el estudiante

@login_required
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
@login_required
def ver_estudiantes(request):

    todosLosEstudiantes = Estudiante.objects.all()

    return render(request, "AppCoder/ver_estudiantes.html", {'todosLosEstudiantes': todosLosEstudiantes})


@login_required
def borrar_estudiante(request, nombre_estudiante):
    borrar_a_estudiante = Estudiante.objects.get(nombre=nombre_estudiante)
    borrar_a_estudiante.delete()

    todos = Estudiante.objects.all()

    return render(request, "AppCoder/ver_estudiantes.html", {'todosLosEstudiantes': todos})


# Buscar el estudiante

@login_required
def buscar_estudiante(request):
    return render(request, "AppCoder/buscar_estudiante.html")

@login_required
def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda

@login_required
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

@login_required
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
@login_required
def ver_entregas(request):

    todosLosEntregables = Entregable.objects.all()

    return render(request, "AppCoder/ver_entregas.html", {'todosLosEntregables': todosLosEntregables})


# Borrar entregables

@login_required
def borrar_entregable(request, nombre_entregable):
    borrar_a_entregable = Entregable.objects.get(nombre=nombre_entregable)
    borrar_a_entregable.delete()

    todos = Entregable.objects.all()

    return render(request, "AppCoder/ver_entregas.html", {'todosLosEntregables': todos})


# Buscar los entregables

@login_required
def buscar_entregable(request):
    return render(request, "AppCoder/buscar_entregable.html")

@login_required
def buscar(request):

    respuesta = f'Última busqueda: {request.GET["apellido"]}'

    return HttpResponse(respuesta)

# Resultado de la busqueda
@login_required
def resultado_entregable(request):
        
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        lista_estudiantes = Entregable.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/resultado_entregable.html", {'valor':nombre, "lista_estudiantes": lista_estudiantes})
        
    else:   

        respuesta = f'Última busqueda: {request.GET["nombre"]}'

    return render(request, "AppCoder/buscar_entregable.html", {"respuesta": respuesta})


# Vistas basadas en clases

class EstudianteLista(ListView):
    model = Estudiante


# Agregamos funciones de usuario

# Inicio de sesión
def login_view(request):
    if request.method == 'POST':

        form_inicio = AuthenticationForm(request, data = request.POST)

        if form_inicio.is_valid():

            info = form_inicio.cleaned_data
            usuario = info.get('username')
            contra = info.get('password')

            user = authenticate(request, username = usuario, password = contra)

            if user:
                login(request, user)

                print(user)

                return render(request, "AppCoder/inicio.html", {'usuario': user})
            
            else:
                return render(request, "AppCoder/inicio.html", {'mensaje': 'Datos Incorrectos!'})
        
    form_inicio = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form': form_inicio})

# Cerrar sesión
@login_required
def logout_view(request):

    LogoutView(request)

    return render(request, "AppCoder/inicio.html", {'mensaje': 'Sesión Cerrada!'})

# Crear un usuario

def create_user(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            form.save()
            return render(request, "AppCoder/inicio.html", {'mensaje': f'Usuario {username} Creado'})
        
    else:

        form = UserCreationForm()

    return render(request, "AppCoder/registro.html", {'form': form})

# Edicion de perfil


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST)

        if form.is_valid():

            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"form": form, "usuario": usuario})

# Funcion para agregar un avatar al perfil deseado.
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuario = request.user
            imagen = form.cleaned_data['imagen']
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            # Redirigir a alguna página de éxito o realizar alguna otra acción
            return render(request, "AppCoder/inicio.html")  # Asegúrate de reemplazar 'nombre_de_la_vista_de_exito' con la vista que desees

    else:
        form = AvatarFormulario()
    
    return render(request, "AppCoder/agregarAvatar.html", {"form": form})