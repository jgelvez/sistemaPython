from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crearLibros, name='crear'),
    path('libros/editar', views.editarLibros, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
