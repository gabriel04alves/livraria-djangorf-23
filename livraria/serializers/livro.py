from rest_framework.serializers import ModelSerializer, SlugRelatedField
from livraria.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer

class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta: 
        model = Livro 
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco", "capa", "categoria"]