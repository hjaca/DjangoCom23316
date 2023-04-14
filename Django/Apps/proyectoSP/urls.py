"""Apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('add_user', views.add_user, name="Add" ),
    path('del_user', views.del_user, name="Del" ),
    path('mod_user', views.mod_user, name="Mod" ),
    path('show_user', views.show_user, name="Show" ),
    path('saludar/<str:nombre>', views.saludar, name="saludar" ),
    path('alumnos/2023', views.alumnos2023, name="alumnos2023" ),
    path('docentes/<int:year>', views.docentes_by_year, {'curso': 'Django'}, name="docentes_by_year" ),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/$', views.alumnos_by_year, name="alumnos_by_year" ),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.alumnos_by_year_month, name="alumnos_by_year_month" ),
    path('alta_alumno', views.alta_alumno, name="alta_alumno" ),
    path('baja_alumno', views.baja_alumno, name="baja_alumno" ),
]
