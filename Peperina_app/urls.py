
from django.urls import path, include
from . import views
from django.contrib import admin





urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('admin/', admin.site.urls),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),  # ← usa pk
    path("agregar-producto/", views.agregar_producto, name="agregar_producto"),
    

    
    
    
]

