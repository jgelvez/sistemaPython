from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

def index(request):
    return render(request, 'paginas/index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crearLibros(request):
    return render(request, 'libros/crear.html')

def editarLibros(request):
    return render(request, 'libros/editar.html')
# Create your views here.
