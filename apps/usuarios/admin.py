from django.contrib import admin
from .models import Admin, Docente, Estudiante, Usuarios

# Register your models here.
admin.site.register(Admin),
admin.site.register(Docente),
admin.site.register(Estudiante),
admin.site.register(Usuarios),