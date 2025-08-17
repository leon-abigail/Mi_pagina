from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        help_text="Usaremos tu email para comunicaciones sobre tu cuenta."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Repetir contraseña",
        }
        help_texts = {
            "username": "Usá letras, números y @/./+/-/_",
            "password1": (
                "Tu contraseña debe tener al menos 8 caracteres, no ser demasiado común ni demasiado similar a tu información personal, "
                "y no puede ser completamente numérica."
            ),
            "password2": "Repetí la misma contraseña para confirmarla.",
        }
        error_messages = {
            "username": {
                "unique": "Ese nombre de usuario ya existe.",
                "invalid": "Ingresá un nombre de usuario válido.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Placeholders bonitos y clases si querés
        self.fields["username"].widget.attrs.update({"placeholder": "Nombre de usuario"})
        self.fields["email"].widget.attrs.update({"placeholder": "correo@ejemplo.com"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Contraseña"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Repetir contraseña"})
