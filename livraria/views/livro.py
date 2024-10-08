from rest_framework import viewsets
from livraria.models import Livro
from livraria.serializers import LivroSerializer, LivroListSerializer, LivroDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter


class LivroFilter(FilterSet):
    categoria = CharFilter(field_name="categoria__descricao", lookup_expr="exact")
    editora = CharFilter(field_name="editora__nome", lookup_expr="exact")
    class Meta:
        model = Livro
        fields = ("categoria", "editora")

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LivroFilter

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action in "retrieve":
            return LivroDetailSerializer
        return LivroSerializer