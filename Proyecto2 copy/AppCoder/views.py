from django.shortcuts import render
from AppCoder.models import curso, ALumnos, Profesores
from django.http import HttpResponse
from django.template import loader 
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario
# Create your views here.

def inicio(request):
    return render(request , "padre.html")   

# Modelo curso:
def cursos(request):
    return render(request, "cursos.html")

def ver_cursos(request):
    cursox = curso.objects.all()
    dicc = {"cursos":cursox}
    plantilla = loader.get_template("ver_cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso(request,nombre):
    cursox = curso(nombre=nombre, camada=234512)
    cursox.save()
    texto = f'Se guardo el curso en en mi BD: {curso.nombre} {curso.camada}'
    return HttpResponse(texto)

def curso_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Curso = curso( nombre=datos['nombre'], camada=datos['camada'])
            Curso.save()
            return render(request, 'formulario.html')
    return render(request, 'formulario.html')

def buscar_curso(request):
    return render(request, 'buscar_curso.html')

def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

# Modelo Alumnos:
def alumnos(request):
    return render(request, 'alumnos.html')

def ver_alumnos(request):
    alumnos = ALumnos.objects.all()
    dicc_alumnos = {'alumnos':alumnos}
    plantilla_alumnos = loader.get_template('ver_alumnos.html')
    documento_alumnos = plantilla_alumnos.render(dicc_alumnos)
    return HttpResponse(documento_alumnos)

def alta_alumno(request):
    alumno = ALumnos(nombre_alumno=nombre, apellido_alumno=apellido, edad_alumno=edad)
    alumno.save()
    texto = f'Se guardo el alumno en la BD: {ALumnos.nombre_alumno} {ALumnos.apellido_alumno} {ALumnos.edad_alumno}'
    return HttpResponse(texto)

def alumno_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Alumno = ALumnos( nombre_alumno=datos['nombre_alumno'], apellido_alumno=datos['apellido_alumno'], edad_alumno=datos['edad_alumno'])
            Alumno.save()
            return render(request, 'formulario_alumno.html')
    return render(request, 'formulario_alumno.html')

def buscar_alumno(request):
    return render(request, 'buscar_alumno.html')

def buscar_a(request):

    if request.GET["nombre_alumno"]:
        nombre_alumno = request.GET["nombre_alumno"]
        cursos = curso.objects.filter(nombre_alumno__icontains= nombre_alumno)
        return render(request, "resultado_busqueda_a.html", {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")

# Modelo Profesores
def profesores(request):
    return render(request, 'profesores.html')

def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc_profesores= {'profesores':profesores}
    plantilla_profesores = loader.get_template('ver_profesores.html')
    documento_profesores = plantilla_profesores.render(dicc_profesores)
    return HttpResponse(documento_profesores)

def alta_profesor(request):
    profesor = Profesores(nombre_prof=nombre, apellido_ptof=apellido, curso_prfo=curso)
    profesor.save()
    texto = f'Se guardo el Profesor en la BD: {Profesores.nombre_prof} {Profesores.apellido_prof} {Profesores.curso_prfo}'
    return HttpResponse(texto)

def profesor_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Profesor = Profesores( nombre_prof=datos['nombre_prof'], apellido_prof=datos['apellido_prof'], curso_prfo=datos['curso_prfo'])
            Profesor.save()
            return render(request, 'formulario_profesor.html')
    return render(request, 'formulario_profesor.html')