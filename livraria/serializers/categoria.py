from rest_framework.serializers import ModelSerializer
from livraria.models import Categoria

# transforma o objeto do db em um json
class CategoriaSerializer(ModelSerializer):
    class Meta: 
        model = Categoria #define o model que será serializado 
        fields = "__all__" #define os campos que serão serializados