from django.shortcuts import render
from django.http import HttpResponse
from models import Profesor

# Create your views here.

def profe_nuevo(request):
    profeN = Profesor(nombre="Juan", apellido="Perez", email="q2Z0u@example.com", profesion="Ingeniero")
    profeN.save()

    return HttpResponse('Hemos guardado al profesor {}')


