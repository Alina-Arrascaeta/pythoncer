from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from .forms import *

# Create your views here.

def index(request):
    return render(request, "app/base.html")

def ipa(request):
    return render(request, "app/ipa.html")

def rubia(request):
    return render(request, "app/rubia.html")


def cliente(request):
    return render(request, "app/cliente.html")


def ipa(request):
    ctx = {"db": Ipa.objects.all()}
    return render(request, "app/ipa.html", ctx)

def rubia(request):
    ctx = {"db": Rubia.objects.all()}
    return render(request, "app/rubia.html", ctx)

def cliente(request):
    ctx = {"db": Cliente.objects.all()}
    return render(request, "app/cliente.html", ctx)



def formIpa(request):
    if request.method == "POST":
        curso = Ipa(nombre=request.POST['nombre'], precio=request.POST['precio'])
        curso.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/cursoForm.html")

def formIpa2(request):
     if request.method == "POST":
        miForm = formIpa(request.POST)
        if miForm.is_valid: 
             informacion = miForm.cleaned_data
             curso = Ipa(nombre=informacion['nombre'], precio=informacion['precio'])
             curso.save()
             return render(request, "app/base.html")

     else:
         miForm = formIpa()
        
        
         return render(request, "app/form_ipa2.html", {"form":miForm})

def buscarIpa(request):
    return render(request, "app/buscarIpa.html")

def buscar2(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        cursos = Ipa.objects.filter(precio__icontains=precio)
        return render(request,
                      "app/resultadosIpa.html",
                     {"precio":precio, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")

def buscarRubia(request):
    return render(request, "app/rubia.html")

def buscar3(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        cursos = Rubia.objects.filter(precio__icontains=precio)
        return render(request,
                      "app/resultadosIpa.html",
                     {"precio":precio, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")

def buscarCliente(request):
    return render(request, "app/cliente.html")

def buscar4(request):
    if request.GET['apellido']:
        apellido = request.GET['apellido']
        cursos = Cliente.objects.filter(apellido__icontains=apellido)
        return render(request,
                      "app/resultadosCliente.html",
                     {"precio":apellido, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")

def formRubia(request):
    if request.method == "POST":
        curso2 = Rubia(nombre=request.POST['nombre'], precio=request.POST['precio'])
        curso2.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/rubiaForm.html")

def formRubia2(request):
     if request.method == "POST":
        miForm2 = formRubia(request.POST)
        if miForm2.is_valid: 
             informacion = miForm2.cleaned_data
             curso2 = Rubia(nombre=informacion['nombre'], precio=informacion['precio'])
             curso2.save()
             return render(request, "app/base.html")

     else:
         miForm2 = formRubia()
        
        
         return render(request, "app/rubiaForm2.html", {"form":miForm2})


def formCliente(request):
    if request.method == "POST":
        curso = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], telefono=request.POST['telefono'])
        curso.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/clienteForm.html")

def formCliente2(request):
     if request.method == "POST":
        miForm = formCliente(request.POST)
        if miForm.is_valid: 
             informacion = miForm.cleaned_data
             curso = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
             curso.save()
             return render(request, "app/base.html")

     else:
         miForm = formCliente()
        
        
         return render(request, "app/clienteForm2.html", {"form":miForm})
