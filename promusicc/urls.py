from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from instrumentos.views  import InstrumentoViewSet, SubCategoriaViewSet, CategoriaViewSet, TipoInsViewSet


router = DefaultRouter()
router.register(r'instrumentos',InstrumentoViewSet)
router.register(r'subcategoria',SubCategoriaViewSet)
router.register(r'categoria',CategoriaViewSet)
router.register(r'tipoinstrumento',TipoInsViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
