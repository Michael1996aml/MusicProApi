from django.shortcuts import render
from rest_framework import viewsets
from .models import Instrumento, SubCategoria, TipoInstrumento, Categoria
from .serializers import InstrumentoSerializers, SubCategoriaSerializers, CategoriaSerializers, TipoInsSerializers  
# Create your views here.

class InstrumentoViewSet(viewsets.ModelViewSet):
    serializer_class= InstrumentoSerializers
    queryset = Instrumento.objects.all()

class SubCategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= SubCategoriaSerializers
    queryset = SubCategoria.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializers
    queryset = Categoria.objects.all()

class TipoInsViewSet(viewsets.ModelViewSet):
    serializer_class= TipoInsSerializers
    queryset = TipoInstrumento.objects.all()

