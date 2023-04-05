from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Proyecto SP")

def add_user(request):
    return HttpResponse("<h1>Add")

def del_user(request):
    return HttpResponse("<h1>Del")

def mod_user(request):
    return HttpResponse("<h1>Mod")

def show_user(request):
    return HttpResponse("<h1>Show")

def saludar(request, nombre):
    return HttpResponse(f"<h1>Hola, <b> {nombre}  </b>bienvenido a Apps")

def alumnos2023(request, year):
    if year < 2020:
        return HttpResponse("No hay alumnos de ese año")
    
def alumnos_by_year(request, year):
    if int(year) < 2020:
        return HttpResponse("No hay alumnos de ese año")
    else:
        return HttpResponse(f"<h1>Hola, <b> {year}  </b>bienvenido a Apps")
    
def alumnos_by_year_month(request, year, month):
    if int(year) < 2020:
        return HttpResponse("No hay alumnos de ese año")
    else:
        return HttpResponse(f"<h1>Hola, <b> {year}{month}  </b>bienvenido a Apps")

def docentes_by_year(request, year, curso):
    if int(year) < 2020:
        return HttpResponse("No hay alumnos de ese año")
    else:
        return HttpResponse(f"<h1>Hola, <b> {year}  </b>bienvenido a {curso}")
    