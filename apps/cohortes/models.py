from django.db import models

# Create your models here.
class Cohorte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    codigo = models.CharField('Codigo',max_length=50, blank=False, null=False)
    descripcion = models.CharField('Descripcion',max_length=300, blank=False, null=False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)
    fecha_fin = models.DateField('fecha de Finalizacion', null=True, blank=True)

    class Meta:
        verbose_name = 'Cohorte'
        verbose_name_plural = 'Cohortes'
        ordering = ['-nombre']

    def __str__(self):
        return ("Cohorte: "+self.nombre)  
    

class Leccion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('titulo de la lección',max_length=50, blank=False, null=False)
    codigo = models.CharField('Codigo Leccion',max_length=50, blank=False, null=False)
    descripcion = models.CharField('Descripcion',max_length=300, blank=False, null=False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)
    fecha_fin = models.DateField('fecha de Finalizacion', null=True, blank=True)
    cohorte_id = models.OneToOneField(Cohorte,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Leccion'
        verbose_name_plural = 'Lecciones'
        ordering = ['-titulo']

    def __str__(self):
        return ("Leccion: "+self.titulo)  

class Task(models.Model):
    title = models.CharField(max_length=100)
    # Por defecto campo basio si no se escribe nada
    description = models.TextField(blank=True)
    # Crea por defecto la fecha en que se creo
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)  # Campo basio inicialmente
    # Por defecto no todas son importantes
    important = models.BooleanField(default=False)
    # Relaciona el FK del User
    leccion_id = models.ForeignKey(Leccion, on_delete=models.CASCADE)

    def __str__(self):
        return "Tarea: "+self.title