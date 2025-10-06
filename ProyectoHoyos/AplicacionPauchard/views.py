from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from .models import Alumno
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class AlumnoView(View):

    # Crear un despachador de la excepcion csrf cross file para poder ejecutar el metodo POST
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        # Declarar una variable para obtener los datos de todos los alumnos como un objeto de lista de valores
        alumnos = list(Alumno.objects.values()) 
        if len(alumnos)>0: #es por que  si consigue registros, crea un diccionario de datos con la informacion
            datos={'message':"Sucess",'alumnos:':alumnos}
        else:
            datos={'message': "ALUMNO NO ENCONTRADO"}
        return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        # Crear un nuevo registro en nuestro ORM
        Alumno.objects.create(rut=jd['rut'],nombrecompleto=jd['nombrecompleto'],carrera=jd['carrera'])
        datos={'message':"Sucess"}
        return JsonResponse(datos)

    def put(self,request):
        pass

    def delete(self,request):
        pass
