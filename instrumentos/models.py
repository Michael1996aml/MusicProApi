

# Create your models here.
from django.db import models

# Create your models here.
class TipoInstrumento(models.Model):
    nombre = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    tipoInstrumento = models.ForeignKey(TipoInstrumento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Instrumento(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=80)
    precio = models.IntegerField()
    genero = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    oferta = models.BooleanField(default= False)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre