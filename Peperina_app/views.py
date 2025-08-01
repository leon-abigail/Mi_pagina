from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import producto
from .forms import productForm
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'home.html')

def catalogo(request):
    productos = producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = productForm()
    return render(request, 'agregar_producto.html', {'form': form})