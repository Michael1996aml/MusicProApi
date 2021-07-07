from django.contrib import admin
from .models import Instrumento, SubCategoria, TipoInstrumento, Categoria

# Register your models here.
admin.site.register(Instrumento)
admin.site.register(SubCategoria)
admin.site.register(TipoInstrumento)
admin.site.register(Categoria)