from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm


class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user:
            login(self.request, user)
        return response


class CustomLoginView(LoginView):
    """
    Login con tu template y redirecciones limpias.
    """
    template_name = "usuarios/login.html"   # usa tu login aesthético
    redirect_authenticated_user = True      # si ya está logueado, lo manda a home
    next_page = reverse_lazy("home")        # adónde va después de loguear

    # (opcional) contexto extra para el template
    extra_context = {"titulo_pagina": "Iniciar sesión"}


class ProfileView(LoginRequiredMixin, DetailView):
    """
    Perfil básico del usuario actual (solo lectura).
    """
    model = User
    template_name = "registration/perfil.html"
    context_object_name = "perfil"

    def get_object(self, queryset=None):
        # siempre mostramos el usuario logueado
        return self.request.user


def logout_now(request):
    """Cierra sesión con GET/POST y redirige al home."""
    logout(request)
    return redirect("home")
