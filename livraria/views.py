from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria, Editora, Autor
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer
# Create your views here.

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all() #objetos que serão retornados pela view
    serializer_class = CategoriaSerializer #define o serializer que será utilizado para serializar(tratar)

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all() 
    serializer_class = EditoraSerializer 

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 