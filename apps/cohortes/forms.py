from django import forms 
from .models import Cohorte,Leccion,Task

class CohorteForm(forms.ModelForm):
    class Meta:
        model = Cohorte
        fields = ['nombre','codigo','descripcion','fecha_fin']

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields = ['titulo','codigo','descripcion','fecha_fin','cohorte_id']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important' , 'leccion_id']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write a description'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'})
        }
