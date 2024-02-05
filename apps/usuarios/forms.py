from django import forms
from .models import Docente, Estudiante, Admin, Usuarios



class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['nombres','apellidos','tipo_documento','identificacion','correo']
    tipo_documento = forms.ChoiceField(choices=Docente.TIPOS_DOCUMENTO, widget=forms.Select(attrs={'class': 'form-control'}))

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombres','apellidos','tipo_documento','identificacion','correo']
    tipo_documento = forms.ChoiceField(choices=Docente.TIPOS_DOCUMENTO, widget=forms.Select(attrs={'class': 'form-control'}))

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombres','apellidos','tipo_documento','identificacion','correo']
    tipo_documento = forms.ChoiceField(choices=Docente.TIPOS_DOCUMENTO, widget=forms.Select(attrs={'class': 'form-control'}))

class UsuariosForm(forms.ModelForm):

    password1 = forms.CharField(label="contraseña",widget=forms.PasswordInput(
        attrs = {
            'class': 'form_control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label="contraseña",widget=forms.PasswordInput(
        attrs = {
            'class': 'form_control',
            'placeholder': 'Confirme su contraseña',
            'id': 'password2',
            'required':'required'
        }
    ))
    class Meta:
        model = Usuarios
        fields = ('username','nombres','apellidos','identificacion','correo','imagen','usuario_activo')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'identificacion': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su identificacion'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su foto de perfil'
                }
            ),
            'usuario_activo': forms.CheckboxInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Usuario activo'
                }
            ),
        }
