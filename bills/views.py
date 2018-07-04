from django.shortcuts import render
from .forms import NewBillForm
from .models import Bill
from datetime import datetime
from django.http import HttpResponseRedirect

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
    #context contiene la lista de anuncios
    context = {'list_bills':list_bills,'form':form }
    return render(request, 'bills/index.html', context)




