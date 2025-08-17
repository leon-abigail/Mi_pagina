from django import forms
from .models import Producto, Categoria, Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'marca', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'style': 'width:100%; padding:8px; border-radius:6px;'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción (opcional)', 'rows':3, 'style': 'width:100%; padding:8px; border-radius:6px;'}),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'style': 'width:150px; padding:8px; border-radius:6px;'}),
            'categoria': forms.Select(attrs={'style': 'padding:8px; border-radius:6px;'}),
            'marca': forms.Select(attrs={'style': 'padding:8px; border-radius:6px;'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

  