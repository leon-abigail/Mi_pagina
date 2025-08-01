
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    

]

