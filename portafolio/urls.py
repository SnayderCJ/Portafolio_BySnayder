from django.urls import path
from . import views

app_name = 'portafolio'  # Nombre de la aplicación (importante para usar '{% url %}' en plantillas)

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
]