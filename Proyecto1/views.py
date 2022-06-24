from django.http import HttpResponse
from django.template import Context, Template
import datetime

def saludar (request):
    return HttpResponse ("Hola mundo")

def segunda_vista (request):
    return HttpResponse ("Esta es la segunda vista")

def dia_de_hoy (request):
    
    dia = datetime.datetime.now()
    cadena= f"hoy es: {dia}"
    return HttpResponse(cadena)

def saludo_con_nombre (self, nombre):
    documento_de_texto = HttpResponse(f"Hola, mi nombre es: {nombre}")
    return HttpResponse(documento_de_texto)

def anio_de_nacimiento (self, edad):
    anio = datetime.date.today().year
    respuesta= HttpResponse(f"Tu año de nacimiento es: {int(anio) -int(edad)}")
    return HttpResponse(respuesta)

#sino todo junto
#def canio_de_nacimiento(self, edad):
#    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probando_html(self):
    archivo=open("M:/My Drive/Cursos/Coderhouse/Python/VisualStudio/Clase 17/Proyecto1/Templates/template1.html")

    plantilla= Template(archivo.read())
    archivo.close()

    contexto= Context()

    documento= plantilla.render(contexto)

    return HttpResponse(documento)