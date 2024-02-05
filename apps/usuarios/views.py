from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import DocenteForm,  EstudianteForm, AdminForm, UsuariosForm, Usuarios
from django.contrib.auth.decorators import login_required
from .models import UsuarioManager
def home(request):
    return render(request, "index.html")

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('index')
    
def signup(request): #Registro de user
    if request.method == 'GET':
        return render(request, 'usuarios/admin/signup.html', {
            'form': UsuariosForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, 'usuarios/admin/signup.html', {
                    'form': UsuariosForm,
                    'error': 'Username already exists'
                })
        return render(request, 'usuarios/admin/signup.html', {
            'form': UsuariosForm,
            'error': 'Password do not match'
        })
    
@login_required 
def registro(request): #Registro de user
    if request.method == 'GET':
        return render(request, 'usuarios/admin/registro.html', {
            'form': UsuariosForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = UsuarioManager.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, 'usuarios/admin/registro.html', {
                    'form': UsuariosForm,
                    'error': 'Username already exists'
                })
        return render(request, 'usuarios/admin/registro.html', {
            'form': UsuariosForm,
            'error': 'Password do not match'
        })
        
def signuout(request):
    logout(request)
    return redirect('index')


def registrarDocente(request):
    if request.method == 'POST': #Validar que sea un metodo post
        register = DocenteForm(request.POST) #variable que guarda la infromacion obtenida del metodo post. de la consulta request, en nuestro form
        print(request.POST) #mostrar en TERMINAL al ENVIAR DATOS
        if register.is_valid(): #validamos que los datos sean validos
            register.save()
            return redirect("index")
    else: #cada vez que se recarge la pagina me enviara la variable autor_form con el modelo de BD obtenido de la classe formulario AutorForm
        register=DocenteForm()
        print(register) #mostrar en TERMINAL al RECARGAR
    return render(request, "usuarios/admin/register.html",{'register_doc': register}) # retonar un renderizado en el html establecido, con la variable que muestra los datos del formulario autor_form

def registrarAdministrador(request):
    if request.method == 'POST': 
        register_admin = AdminForm(request.POST) 
        print(request.POST) 
        if register_admin.is_valid(): 
            register_admin.save()
            return redirect("index")
    else: 
        register_admin=AdminForm()
        print(register_admin)
    return render(request, "usuarios/admin/register.html",{'register_admin': register_admin}) 

def registrarEstudiante(request):
    if request.method == 'POST': 
        register = EstudianteForm(request.POST) 
        print(request.POST) 
        if register.is_valid(): 
            register.save()
            return redirect("index")
    else: 
        register=EstudianteForm()
        print(register)
    return render(request, "usuarios/admin/register.html",{'register_es': register}) 

