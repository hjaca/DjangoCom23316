from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(request.method)

    listado_alumnos = [
        {
            'name': 'Maria',
            'last_name': 'Luna',
            'age': 20,
            'valid': False,
        },
        {
            'name': 'John',
            'last_name': 'Star',
            'age': 30,
            'valid': False,
        },
        {
            'name': 'Juan',
            'last_name': 'Sol',
            'age': 40,
            'valid': True,
        },
    ]

    alumno_ficticio = {
        'name': 'Cata',
        'last_name': 'Reca',
        'age': 24,
    }
    
    context = {
        'first_name': 'Luis',
        'last_name': 'Monte',
        'student': alumno_ficticio, 
        'listado_alumnos': listado_alumnos,
    }

    return render(request, 'proyectoSP/index.html', context)

def baja_alumno(request):
#    return HttpResponse("<h1>Add")
    return render(request, 'proyectoSP/baja_alumno.html')

def alta_alumno(request):
#    return HttpResponse("<h1>Del")
    return render(request, 'proyectoSP/alta_alumno.html')

def modif_alumno(request):
    return HttpResponse("<h1>Mod")

def show_alumno(request):
    return HttpResponse("<h1>Show")

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
    