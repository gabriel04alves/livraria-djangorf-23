from rest_framework.serializers import ModelSerializer
from livraria.models import Categoria
from livraria.models import Editora
from livraria.models import Autor

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