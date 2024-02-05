#Importarmos libreria para las urls
from django.urls import path
from .views import crearLeccion, crearCohorte
from ..usuarios.views import home
urlpatterns = [
    path('register_coh/', crearCohorte, name='registro_cohorte'),
    path('register_lec/', crearLeccion, name='registro_leccion'),
    #path('', home, name='index'),
]  