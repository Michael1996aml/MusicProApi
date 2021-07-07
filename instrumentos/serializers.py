from rest_framework import serializers
from .models import Instrumento,SubCategoria,Categoria,TipoInstrumento

class InstrumentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = '__all__'

class SubCategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = '__all__'
        
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TipoInsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoInstrumento
        fields = '__all__'