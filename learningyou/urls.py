"""
URL configuration for learningyou project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.usuarios.views import home, registrarAdministrador, registrarDocente, registrarEstudiante, signin, signuout, signup, registro
from apps.cohortes.views import crearCohorte, crearLeccion
from apps.cohortes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('apps.usuarios.urls','usuarios'))),
    path('cohortes/', include(('apps.cohortes.urls','cohortes'))),
    path('', home, name='index'),
    #usuarios
    path('registro/admin/', registrarAdministrador, name='registro_admin'),
    path('registro/docente/', registrarDocente, name='registro_docente'),
    path('registro/estudiante/', registrarEstudiante, name='registro_estudiante'),
    path('registro/signup/', signup, name="signup"),
    path('logout/', signuout, name="logout"),
    path('signin/', signin, name="signin"),
    path('registro_users/', registro, name="registro_usuarios"),
    #cohortes
    path('registro/cohorte/', crearCohorte, name='registro_cohorte'),
    path('registro/leccion/', crearLeccion, name='registro_leccion'),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed', views.tasks_completed, name="tasks_completed"),
    path('tasks/create', views.create_task, name="create_task"),
    path('tasks/<int:task_id>', views.tasks_detail, name="tasks_detail"),
    path('tasks/<int:task_id>/complete', views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_task"),
    path('cohortes/', views.cohortes, name="cohortes"),

]
