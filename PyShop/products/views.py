from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Toda view function tem que receber um parâmetro, request eh o pedido HTTP do navegador.
def index(request):
    # Metodo que pegara todos os atributos da classe Product
    products = Product.objects.all()
    # render() renderiza um modelo/template , com argumentos ( request , 'nome' , {dicionario} )
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')
