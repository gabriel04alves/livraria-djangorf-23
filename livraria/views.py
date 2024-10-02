from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer, LivroListSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all() #objetos que serão retornados pela view
    serializer_class = CategoriaSerializer #define o serializer que será utilizado para serializar(tratar)
    permission_classes = [IsAuthenticated]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all() 
    serializer_class = EditoraSerializer 

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer 

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action in "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
    
