from rest_framework.serializers import ModelSerializer
from livraria.models import Categoria, Editora, Autor, Livro

# transforma o objeto do db em um json
class CategoriaSerializer(ModelSerializer):
    class Meta: 
        model = Categoria #define o model que será serializado 
        fields = "__all__" #define os campos que serão serializados
        
class EditoraSerializer(ModelSerializer):
    class Meta: 
        model = Editora 
        fields = "__all__"
        
class AutorSerializer(ModelSerializer):
    class Meta: 
        model = Autor 
        fields = "__all__"
        
class LivroSerializer(ModelSerializer):
    class Meta: 
        model = Livro 
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco"]