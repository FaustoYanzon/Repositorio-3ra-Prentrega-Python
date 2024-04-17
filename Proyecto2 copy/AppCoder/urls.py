from django.urls import path
from . import views

urlpatterns = [
    # Paths Modelo Curso
    path('',views.inicio, name="home"),
    path( 'cursos', views.cursos, name = 'cursos'),
    path('ver_cursos/', views.ver_cursos, name="ver_cursos" ),
    # path('alta_curso1/', views.alta_curso1),
    path('alta_curso', views.curso_formulario, name='alta_curso'),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar, name="buscar"),
    
    # Paths Modelo Alumnos
    path('alumnos/', views.alumnos, name = 'alumnos' ),
    path('ver_alumnos', views.ver_alumnos, name = 'ver_alumnos'),
    path('alta_alumno', views.alumno_formulario, name='alta_alumno'),
    path("buscar_alumno", views.buscar_alumno, name="buscar_alumno"),
    path("buscar_a", views.buscar_a, name="buscar_a"),
    
    # Paths Modelo Profesores
    path('profesores', views.profesores, name='profesores'),
    path('ver_profesores', views.ver_profesores, name = 'ver_profesores'),
    path('alta_profesor', views.profesor_formulario, name='alta_profesor'),
]
