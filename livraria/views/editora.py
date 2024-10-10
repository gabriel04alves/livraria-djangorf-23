from rest_framework.viewsets import ModelViewSet
from livraria.models import Editora
from livraria.serializers import EditoraSerializer
from livraria.serializers import LivroSerializer, LivroListSerializer, LivroDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter

class EditoraFilter(FilterSet):
    nome = CharFilter(field_name="nome", lookup_expr="icontains")
    class Meta:
        model = Editora
        fields = ["nome"]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all() 
    serializer_class = EditoraSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = EditoraFilter
    search_fields = ["nome"]
    ordering_fields = ["nome"]
    ordering = ["nome"]

