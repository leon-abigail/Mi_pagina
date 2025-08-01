from django.shortcuts import render, redirect
from django.http import HttpResponse




def home(request):
    return render(request, 'home.html')

def lista_productos(request):
    from .models import producto
    productos = producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})