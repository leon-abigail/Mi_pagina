from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegistrationView, logout_now
from usuarios.views import CustomLoginView, UserRegistrationView, ProfileView, logout_now

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/",  auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),

    # Vista que ya tenías
    path("salir/", logout_now, name="logout_now"),

    # Alias para que /usuarios/logout/ también funcione
    path("logout/", logout_now, name="logout"),
    path("perfil/", ProfileView.as_view(), name="profile")
]