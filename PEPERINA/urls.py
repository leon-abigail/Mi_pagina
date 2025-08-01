from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Peperina_app.urls')),  # Asegurate de haber creado este archivo también
]
