from django.contrib import admin
from django.urls import path
from AppFinal.views import login_request, blogDetalle, blogLista, crearBlog, Perfil, cerrarSesion, ProfileView, pokemon, fizzbuzz, generador_contraseñas
from AppFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('pokemon/', views.pokemon, name='Pokemon'),
    path('fizzbuzz/', views.fizzbuzz, name='Fizzbuzz'),
    path('escalones/', views.escalones_view, name='Escalones'),
    path('generador/', views.generador_contraseñas, name='Generador_Contraseñas'),
    path('padre', views.padre, name='Padre'),
    path('about', views.about, name='About'),
    path('accounts/login', views.login_request, name="Login"),
    path('accounts/register', views.register, name='Register'),
    path('logout/', cerrarSesion, name='logout'),
    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html'), name='Logout'),
    path('blogs/', blogLista, name='blogLista'),
    path('crearBlog', crearBlog, name='crearBlog'),
    path('blog/<int:blog_id>/', blogDetalle, name='blogDetalle'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('perfil/', views.perfilUsuario, name='Perfil'),
]