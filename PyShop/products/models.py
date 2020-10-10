from django.db import models


# Definindo 'Product' como subclasse de 'Model' ( uma classe do modulo 'model')
# Isso vai acabar sendo parecido com classe modelo do Entity Framework, para modelar a tabela de um BD.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=100)
    discount = models.FloatField()
