from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carreras/', views.lista_carreras, name='lista_carreras'),
    path('carreras/crear/', views.crear_carrera, name='crear_carrera'),
    path('carreras/editar/<int:id>/', views.editar_carrera, name='editar_carrera'),
    path('carreras/eliminar/<int:id>/', views.eliminar_carrera, name='eliminar_carrera'),
]