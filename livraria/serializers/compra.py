from rest_framework.serializers import (
    CharField,
    CurrentUserDefault, 
    HiddenField, 
    ModelSerializer,
    SerializerMethodField,
)
from livraria.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco
    
    class Meta: 
        model = ItensCompra
        fields = ["livro", "quantidade", "total"]
        depth = 2   # depth=2 inlui detalhes dos relacionamentos, aumentando a profundidade da serialização.
                    # Se depth=1 fosse usado incluiria os detalhes dos relacionamentos diretos (pk's).

class CompraSerializer(ModelSerializer):
    
    # O parâmetro source indica qual campo do model será utilizado para preencher o campo do serializer.
    # O parâmetro read_only indica que o campo em questão não será utilizado para atualizar a model.
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    total_compra = SerializerMethodField() 
    
    def get_total_compra(self, obj):
        total_compra = 0 
        for item in obj.itens.all():
            total_compra += item.livro.preco * item.quantidade 
        return total_compra
    
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "itens", "total_compra")

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta: 
        model = ItensCompra
        fields = ("livro", "quantidade")

class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)

    class Meta:
        model = Compra 
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra
    
    # não funciona com patch 
    def update(self, instance, validated_data):
        itens_data = validated_data.pop("itens")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        for item_data in itens_data:
            item_id = item_data.get("id")
            if item_id:  
                item = ItensCompra.objects.get(id=item_id, compra=instance)
                item.quantidade = item_data.get("quantidade", item.quantidade)
                item.livro = item_data.get("livro", item.livro)
                item.save()
            else:  
                ItensCompra.objects.create(compra=instance, **item_data)

        instance.save()
        return instance


