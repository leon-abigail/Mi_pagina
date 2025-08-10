from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from decimal import Decimal, InvalidOperation
from django.contrib.auth.decorators import permission_required

from .models import Producto, Categoria, Marca
from .forms import ProductoForm
from django.http import HttpResponse

def home(request):
    # muestra algunos productos destacados (6 últimos)
    destacados = Producto.objects.all().order_by('-id')[:6]
    return render(request, 'home.html', {'destacados': destacados})

def lista_productos(request):
    q = request.GET.get('q', '').strip()
    categoria_slug = request.GET.get('categoria', '').strip()
    marca_id = request.GET.get('marca', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    productos = Producto.objects.all().select_related('categoria', 'marca')

    if q:
        productos = productos.filter(Q(nombre__icontains=q) | Q(descripcion__icontains=q))

    if categoria_slug:
        productos = productos.filter(categoria__slug=categoria_slug)

    if marca_id:
        productos = productos.filter(marca__id=marca_id)

    try:
        if min_price:
            productos = productos.filter(precio__gte=Decimal(min_price))
        if max_price:
            productos = productos.filter(precio__lte=Decimal(max_price))
    except InvalidOperation:
        pass

    productos = productos.order_by('nombre')

    paginator = Paginator(productos, 9)  # 9 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    context = {
        'page_obj': page_obj,
        'productos': page_obj.object_list,
        'categorias': categorias,
        'marcas': marcas,
        'q': q,
        'categoria_slug': categoria_slug,
        'marca_id': marca_id,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'lista_productos.html', context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def lista_categorias(request):
    return render(request, 'lista_categorias.html')
