from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter

class CategoriaFilter(FilterSet):
    descricao = CharFilter(field_name="descricao", lookup_expr="icontains")
    class Meta:
        model = Categoria
        fields = ["descricao"]

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all() #objetos que serão retornados pela view
    serializer_class = CategoriaSerializer #define o serializer que será utilizado para serializar(tratar)
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CategoriaFilter
    search_fields = ["descricao"]
    ordering_fields = ["descricao"]
    ordering = ["descricao"]