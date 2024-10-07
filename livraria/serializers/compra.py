from rest_framework.serializers import ModelSerializer, CharField
from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    
    # O parâmetro source indica qual campo do model será utilizado para preencher o campo do serializer.
    # O parâmetro read_only indica que o campo em questão não será utilizado para atualizar a model.
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    
    class Meta:
        model = Compra
        fields = "__all__"