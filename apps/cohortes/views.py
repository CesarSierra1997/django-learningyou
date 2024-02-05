from django.shortcuts import render, redirect, get_object_or_404
from .forms import CohorteForm, LeccionForm, TaskForm, Task, Cohorte
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def crearCohorte(request):
    if request.method == 'POST': #Validar que sea un metodo post
        cohorte_form = CohorteForm(request.POST) #variable que guarda la infromacion obtenida del metodo post. de la consulta request, en nuestro form
        print(request.POST) #mostrar en TERMINAL al ENVIAR DATOS
        if cohorte_form.is_valid(): #validamos que los datos sean validos
            cohorte_form.save()
            return redirect("index")
    else: #cada vez que se recarge la pagina me enviara la variable autor_form con el modelo de BD obtenido de la classe formulario AutorForm
        cohorte_form=CohorteForm()
        print(cohorte_form) #mostrar en TERMINAL al RECARGAR
    return render(request, "usuarios/admin/register_coh.html",{'formulario_cohorte': cohorte_form}) # retonar un renderizado en el html establecido, con la variable que muestra los datos del formulario autor_form

def crearLeccion(request):
    if request.method == 'POST': #Validar que sea un metodo post
        leccion_form = LeccionForm(request.POST) #variable que guarda la infromacion obtenida del metodo post. de la consulta request, en nuestro form
        print(request.POST) #mostrar en TERMINAL al ENVIAR DATOS
        if leccion_form.is_valid(): #validamos que los datos sean validos
            leccion_form.save()
            return redirect("index")
    else: #cada vez que se recarge la pagina me enviara la variable autor_form con el modelo de BD obtenido de la classe formulario AutorForm
        leccion_form=LeccionForm()
        print(leccion_form) #mostrar en TERMINAL al RECARGAR
    return render(request, "usuarios/admin/register_lec.html",{'formulario_leccion': leccion_form}) # retonar un renderizado en el html establecido, con la variable que muestra los datos del formulario autor_form

def cohortes(request): #Vista de tareas
    # tasks = Task.objects.all() #Para mostrar todos los usurios SIRVE PARA VISTA DOCENTE
    # Muestra las tareas del un usuario en espeficico y solo las que a un estan por completar
    coh = Cohorte.objects.all().order_by('-fecha_creacion')
    return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/cohortes.html', {
        'form': coh
    })

@login_required
def tasks(request): #Vista de tareas
    # tasks = Task.objects.all() #Para mostrar todos los usurios SIRVE PARA VISTA DOCENTE
    # Muestra las tareas del un usuario en espeficico y solo las que a un estan por completar
    tasks = Task.objects.filter(datecompleted__isnull=True)
    return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/tasks.html', {
        
        'tasks': tasks
    })

def tasks_completed(request): #Vista de Tareas completadas
    tasks = Task.objects.filter(datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/tasks_completed.html', {
        'tasks': tasks
    })

def create_task(request): #Crear tarea
    if request.method == 'GET':
        return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/create_task.html', {
                'form': TaskForm,
                'error': 'Please provide valida data'
            })
        
def tasks_detail(request, task_id): #Actualizar tareas
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id)#Busca por el id de la tarea y el usuario debe ser igual 
        form = TaskForm(instance=task)
        return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/tasks_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:          
            tasks = Task.objects.filter(datecompleted__isnull=True)
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(request.POST, instance=task)
            form.save()
            
            title = Task.objects.get(pk=task_id).title
            task.datecompleted = None
            task.save()

            return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/tasks.html', {
                'msg': 'Actualizacion: ', 
                'title':title,
                'tasks': tasks

            })
        except ValueError:
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(instance=task)
            return render(request, 'C:/Users/cesar/OneDrive/Escritorio/Django/learningyou/apps/usuarios/templates/usuarios/docente/tasks_detail.html', {
                'error': 'Error updatign task',
                'form': form
            })

def complete_task(request, task_id): #Completar Tarea
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect ('tasks')

def delete_task(request, task_id): #Eliminar Tarea
    task = Task.objects.get( pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect ('tasks')
   
