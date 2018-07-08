from django.shortcuts import render, redirect
from .forms import NewBillForm
from .models import Bill
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    #corrobora si request viene de un form con metodo post
    if request.method == 'POST':
        #obteniendo la data
        new_bill_form = NewBillForm(request.POST)
        if new_bill_form.is_valid():
            # preparando los datos p crear un nuevo anuncio
            data = new_bill_form.cleaned_data #se guardan aqui despues de que isvalid es true
            title = data.get('title')
            content = data.get('content')
            author = data.get('author')
            date = datetime.now()
            #conectando con la base de datos. escribiendo datos en una variable a traves de un modelo (objetos)
            b = Bill(date=date, title=title, content=content, author=author)
            b.save()
            return HttpResponseRedirect('/')

    #conectando con la base de datos.leyendo de la base de datos
    list_bills = Bill.objects.all() #crea una lista de diccionario que contiene todos los registros del modelo Bill de la base de datos.
    form = NewBillForm()
    registerForm = UserCreationForm()
    m = getattr(request, '_messages', [])
    #context contiene la lista de anuncios
    context = {'list_bills':list_bills,'form':form, 'registerForm':registerForm, 'messages': m}
    return render(request, 'bills/index.html', context)


def log_in(request):
    username = request.POST['username'] #input name
    password = request.POST['password'] #input contrasena
    user = authenticate(request, username=username, password=password) #verifica nombre y contrasena
    if user is not None: #p comprobar que hay usuario
        login(request, user) #si hay usuario lo logeamos
        messages.success(request, 'You logged in successfully')
    else:
        messages.error(request, 'Invalid username/password')

    return redirect('/')

def register(request):
    f = UserCreationForm(request.POST) #sirve para crear el form, para generar el html que se le mostrara al usuario y p leerlo
    if f.is_valid(): #comprobamos si el form es valido
        f.save() #lo guardamos en la base de datos
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully')
    else:
        messages.error(request, 'The account could not be created')

    return redirect('/')

def log_out(request):
    logout(request)
    messages.success(request, 'You logged out successfully')
    return redirect('/')



