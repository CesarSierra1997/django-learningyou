#Importarmos libreria para las urls
from django.urls import path
from .views import home, registrarDocente, registrarAdministrador, registrarEstudiante, signin, signuout, signup
urlpatterns = [
    path('signin/', signin, name="signin"),
    path('logout/', signuout, name="logout"),
    path('signup/', signup, name="signup"),
    path('registro_docente/', registrarDocente, name='registro_docente'),
    path('registro_admin/', registrarAdministrador, name='registro_admin'),
    path('registro_estudiante/', registrarEstudiante, name='registro_estudiante'),
    path('', home, name='index'),
]  