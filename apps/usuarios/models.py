from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres',max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False, null=False)
    TIPOS_DOCUMENTO = [
        ('cedula', 'Cédula'),
        ('registro', 'Registro Civil'),
        ('pasaporte', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    identificacion = models.CharField('Identificación',max_length=10, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Administradores'
        ordering = ['-nombres']

    def __str__(self):
        return ("TipoDoc: "+self.tipo_documento+" No. "+self.identificacion+" Admin: "+self.nombres+" "+self.apellidos)  

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres',max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False, null=False)
    TIPOS_DOCUMENTO = [
        ('cedula', 'Cédula'),
        ('registro', 'Registro Civil'),
        ('pasaporte', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    identificacion = models.CharField('Identificación',max_length=10, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['-nombres']

    def __str__(self):
        return ("TipoDoc: "+self.tipo_documento+" No. "+self.identificacion+" Docente: "+self.nombres+" "+self.apellidos)  
    
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres',max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False, null=False)
    TIPOS_DOCUMENTO = [
        ('cedula', 'Cédula'),
        ('registro', 'Registro Civil'),
        ('pasaporte', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    identificacion = models.CharField('Identificación',max_length=10, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['-nombres']

    def __str__(self):
        return ("TipoDoc: "+self.tipo_documento+" No. "+self.identificacion+" Estudiante: "+self.nombres+" "+self.apellidos) 

#crear usuario y admin
class UsuarioManager( BaseUserManager):
    def create_user(self, correo, username, nombres,identificacion, apellidos=None, password= None):
        if not correo:
            raise ValueError("El usuario debe tener correo electronico")
        
        usuario = self.model(
            username=username,
            correo = self.normalize_email(correo),
            identificacion = identificacion,
            nombres=nombres,
            apellidos=apellidos)
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,correo,username,identificacion, nombres, apellidos, password):
        usuario = self.create_user(
            correo,
            username=username,
            identificacion = identificacion,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )
        usuario.usuario_admin=True
        usuario.save()
        return usuario

class Usuarios(AbstractBaseUser ):
    id = models.AutoField(primary_key=True)
    username = models.CharField("Nombre de Usuario",unique=True, max_length=50)
    nombres = models.CharField('Nombres',max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=200, blank=False, null=False)
    identificacion = models.CharField('Identificación',max_length=10, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=100, blank=False, null=False)
    imagen = models.ImageField('Foto de perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)
    usuario_activo = models.BooleanField(default=True)
    usuario_admin = models.BooleanField(default=False)
    objects=UsuarioManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['nombres','apellidos','identificacion','correo']

    def __str__(self):
        return "Usuario: "+self+" No. "+self.nombres
    
    def has_perm(self, perm,obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_admin