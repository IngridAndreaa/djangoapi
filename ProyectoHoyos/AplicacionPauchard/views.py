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

    def get(self,request, rut=''):
        if (rut!=''): #para filtrar un unico registro
            alumnos = list(Alumno.objects.filter(rut=rut).values())
            if len(alumnos) > 0:
                persona=alumnos[0]
                datos={'message':"Success" , 'alumno':persona}
            else:
                datos={'message':"ALUMNO NO ENCONTRADO"}
            return JsonResponse(datos)
        else:
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

    def put(self,request,rut):
        jd = json.loads(request.body)
        alumnos = list(Alumno.objects.filter(rut=rut).values())
        if len(alumnos)>0: #es porque si consigue registros
            persona = Alumno.objects.get(rut=rut)
            persona.nombrecompleto = jd['nombrecompleto']
            persona.carrera = jd['carrera']
            persona.save() #guardar el registro
            datos={'message':"Success"}
        else:
            datos={'message':"EL ALUMNO NO EXISTE"}
        return JsonResponse(datos)


    def delete(self,request,rut):
        alumnos = list(Alumno.objects.filter(rut=rut).values())
        if len(alumnos)>0: #si consigue registros
            #proceder a borrar el registro del ORM
            Alumno.objects.filter(rut=rut).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"ALUMNO NO EXISTE"}
        return JsonResponse(datos)


