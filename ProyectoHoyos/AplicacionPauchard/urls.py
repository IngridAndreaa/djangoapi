from django.urls import path
from .views import AlumnoView


urlpatterns = [
    path('alumnosinventario/', AlumnoView.as_view(), name='Alumno_Lista'),
    path('alumnosinventario/<str:rut>', AlumnoView.as_view(), name= 'Alumno')
]