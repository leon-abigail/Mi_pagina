from django import forms
from .models import producto 

class productForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'precio', 'descripcion']