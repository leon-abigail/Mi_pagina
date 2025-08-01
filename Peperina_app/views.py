from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm




def home(request):
    return render(request, 'home.html')

def lista_productos(request):
    from .models import producto
    productos = producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})