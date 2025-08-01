from django.contrib import admin
from .models import producto

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')  # muestra estas columnas en el listado
    search_fields = ('nombre',)  # permite buscar por nombre
    list_filter = ('categoria',)  # filtros por categoría (si tienes)

# Si no quieres usar el decorador, puedes hacer también:
# admin.site.register(Producto, ProductoAdmin)


