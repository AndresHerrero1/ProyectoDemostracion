from django.shortcuts import get_object_or_404, render, redirect
from AppFinal.forms import UserRegisterForm, PerfilForm
from AppFinal.models import Blog, Perfil
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AppFinal.forms import BlogForm, Perfil, UserUpdateForm, ProfileUpdateForm
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import requests
import random
import string


# Create your views here.


def inicio(request):
    return render(request, "AppFinal/inicio.html")

def pages(request):
    return render(request, "AppFinal/pages.html")

def about(request):
    return render(request, "AppFinal/about.html")

def padre(request):
    return render(request, "AppFinal/Padre.html")

def cerrarSesion(request):
    logout(request)
    return redirect('Inicio')

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppFinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppFinal/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppFinal/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppFinal/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppFinal/registro.html" ,  {"form":form})

@login_required
def perfilUsuario(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Tu cuenta ha sido actualizada.')
            return redirect('perfil')
        else:
            messages.error(request, f'Por favor corrige los errores a continuación.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilForm(instance=request.user.perfil)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'AppFinal/perfil.html', context)

def crearBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            direccion = form.cleaned_data['ubicacion']
            # Llamar a la API de OpenStreetMap para obtener las coordenadas geográficas
            response = requests.get(f'https://nominatim.openstreetmap.org/search?q={direccion}&format=json')
            if response.status_code == 200:
                data = response.json()
                if data:
                    # Obtener las coordenadas de la primera coincidencia
                    latitud = data[0]['lat']
                    longitud = data[0]['lon']
                    blog.ubicacion = f'{latitud},{longitud}'
            blog.save()
            return redirect('blogLista')
    else:
        form = BlogForm()
    return render(request, 'AppFinal/crearBlog.html', {'form': form, 'latitud': 0, 'longitud': 0})  # Pasar latitud y longitud en el contexto

def blogLista(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'AppFinal/blogLista.html', context)

def inicio(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'AppFinal/inicio.html', context)

def seccionLista(request):
    blogs = Blog.objects.all()
    template = ('AppFinal/blogLista.html', {'blogs': blogs})
    return render(request, *template)

def blogDetalle(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Obtener las coordenadas de la ubicación del blog si está disponible
    latitud, longitud = 0, 0  # Valores predeterminados
    if blog.ubicacion:
        coordenadas = blog.ubicacion.split(',')
        if len(coordenadas) == 2:
            latitud, longitud = float(coordenadas[0]), float(coordenadas[1])
    
    return render(request, 'blogs/blogDetalle.html', {'blog': blog, 'latitud': latitud, 'longitud': longitud})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'AppFinal/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # otras variables de contexto aquí
        return context
    
from django.shortcuts import render
import requests

def pokemon(request):
    if request.method == 'POST':
        numero = int(request.POST.get('pokemon_number'))
        if numero < 1 or numero > 1025:
            message = "La pokédex va desde el 1 hasta el 1025"
        else:
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
            poke_response = requests.get(poke_url)
            pokemon = poke_response.json()

            nombre = pokemon['name']
            tipos = [type['type']['name'] for type in pokemon['types']]
            habilidades = [ability['ability']['name'] for ability in pokemon['abilities']]
            salud = pokemon['stats'][0]['base_stat']
            ataque = pokemon['stats'][1]['base_stat']
            defensa = pokemon['stats'][2]['base_stat']
            ataque_especial = pokemon['stats'][3]['base_stat']
            defensa_especial = pokemon['stats'][4]['base_stat']
            velocidad = pokemon['stats'][5]['base_stat']

            message = f"El pokémon {nombre} posee los tipos {tipos}. Sus habilidades son {habilidades}, " \
                      f"Sus parámetros son: \n salud: {salud} \n ataque: {ataque} \n defensa: {defensa} \n ataque especial: {ataque_especial} \n defensa especial: {defensa_especial} \n velocidad: {velocidad}"

    else:
        message = ''

    return render(request, 'AppFinal/pokemon.html', {'message': message})

def fizzbuzz(request):
    if request.method == 'POST':
        max_num = int(request.POST['max_num'])
        num_range = range(1, max_num + 1)
        fizzbuzz_lista = []
        for numero in num_range:
            if numero % 3 == 0 and numero % 5 == 0:
                fizzbuzz_lista.append("fizzbuzz")
            elif numero % 3 == 0:
                fizzbuzz_lista.append("fizz")
            elif numero % 5 == 0:
                fizzbuzz_lista.append("buzz")
            else:
                fizzbuzz_lista.append(str(numero))
        context = {'fizzbuzz_lista': fizzbuzz_lista}
        return render(request, 'AppFinal/fizzbuzz.html', context)
    else:
        return render(request, 'AppFinal/fizzbuzz.html', {})
    
def dibujar_escalones(escalones):
    if escalones > 0:
        result = ""
        for escalon in range(escalones + 1):
            espacios = "  " * (escalones - escalon)
            dibujar_escalon = "_" if escalon == 0 else "_|"
            result += f"{espacios}{dibujar_escalon}\n"
    elif escalones < 0:
        result = ""
        for escalon in range(abs(escalones) + 1):
            espacios = " " * ((escalon * 2) - 1)
            dibujar_escalon = "_" if escalon == 0 else "|_"
            result += f"{espacios}{dibujar_escalon}\n"
    else:
        result = "__\n"
    return result

def escalones_view(request):
    if request.method == 'POST':
        escalones = int(request.POST['escalones'])
        output = dibujar_escalones(escalones)
    else:
        output = ""
    return render(request, 'AppFinal/escalones.html', {'output': output})

def generador_contraseñas(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        mayus = request.POST.get('mayus') == 'on'
        numeros = request.POST.get('numeros') == 'on'
        simbolos = request.POST.get('simbolos') == 'on'

        characters = string.ascii_lowercase
        if mayus:
            characters += string.ascii_uppercase
        if numeros:
            characters += string.digits
        if simbolos:
            characters += string.punctuation

        contraseña = ''.join(random.choice(characters) for _ in range(length))
        return render(request, 'AppFinal/generadorContraseña.html', {'contraseña': contraseña})
    else:
        return render(request, 'AppFinal/generadorContraseña.html')