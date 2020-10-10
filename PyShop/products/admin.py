from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    # Criando um tuple com os atributos da classe Product do modulo models
    # Isso basicamente adicionaria tabelas para especificar o que é cada produto no painel adm
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Registrando Product para poder gerenciar produtos no painel de administracao
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)