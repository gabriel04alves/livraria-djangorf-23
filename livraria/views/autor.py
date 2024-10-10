from rest_framework.viewsets import ModelViewSet
from livraria.models import Autor 
from livraria.serializers import AutorSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter

class AutorFilter(FilterSet):
    nome = CharFilter(field_name="nome", lookup_expr="icontains")
    class Meta:
        model = Autor
        fields = ["nome"]

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AutorFilter
    search_fields = ["nome"]
    ordering_fields = ["nome"]
    ordering = ["nome"]