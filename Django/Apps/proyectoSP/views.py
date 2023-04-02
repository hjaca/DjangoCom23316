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