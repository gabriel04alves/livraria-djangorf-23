from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault, 
    HiddenField, 
    ModelSerializer,
    SerializerMethodField
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
    
    def validate(self, data):
        if data["quantidade"] > data["livro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponível em estoque."}
            )
        return data

class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)

    class Meta:
        model = Compra 
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens_data:
            item["preco_item"] = item["livro"].preco
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
    
    # não funciona com patch 
    def update(self, instance, validated_data):
        itens_data = validated_data.pop("itens")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if itens_data:
            instance.itens.all().delete()
            for item in itens_data:
                item["preco_item"] = item["livro"].preco  
                ItensCompra.objects.create(compra=instance, **item)

        instance.save()
        return instance


