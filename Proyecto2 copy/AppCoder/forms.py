from django import forms 

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Alumno_formulario(forms.Form):
    nombre_alumno = forms.CharField(max_length=20)
    apellido_alumno = forms.CharField(max_length=20)
    edad_alumno = forms.IntegerField()

class Profesor_formulario(forms.Form):
    nombre_prof = forms.CharField(max_length=20)
    apellido_prof = forms.CharField(max_length=29)
    curso_prfo = forms.CharField(max_length=30)