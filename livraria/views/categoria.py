from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all() #objetos que serão retornados pela view
    serializer_class = CategoriaSerializer #define o serializer que será utilizado para serializar(tratar)
    permission_classes = [IsAuthenticated]