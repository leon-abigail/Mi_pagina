
from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static  
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('admin/' , admin.site.urls),
    path('productos/', include('productos.urls')),
    

]

