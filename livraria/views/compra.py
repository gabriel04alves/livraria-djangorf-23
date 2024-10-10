from rest_framework.viewsets import ModelViewSet
from livraria.models import Compra
from usuario.models import Usuario
from livraria.serializers import CompraSerializer, CriarEditarCompraSerializer
from livraria.serializers import LivroSerializer, LivroListSerializer, LivroDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter

class CompraFilter(FilterSet): 
    data = CharFilter(field_name="data", lookup_expr="exact")
    class Meta:
        model = Compra
        fields = ["data"]

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompraFilter
    search_fields = ["data"]
    ordering_fields = ["data"]
    ordering = ["data"]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        if usuario.tipo == Usuario.Tipos.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
        # urls.py

        router = DefaultRouter()
        router.register(r'compras', CompraViewSet)

        urlpatterns = [
            path('', include(router.urls)),
        ]

        # To test the filters, you can use a URL like:
        # /compras/?data=2023-10-01