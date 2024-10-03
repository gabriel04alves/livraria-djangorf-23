from django.db import models 
from livraria.models import Autor, Categoria, Editora
from uploader.models import Image

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    # FKs: 
    categoria = models.ForeignKey(
        Categoria, # model associado 
        on_delete=models.PROTECT, # ->impede de apagar uma categoria que possua livros associados 
        related_name="livros" # cria um atributo livros na classe[...]
    )
    editora = models.ForeignKey(
        Editora,
        on_delete=models.PROTECT,
        related_name="livros"
    )
    capa = models.ForeignKey(
        Image, 
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
    
    autores = models.ManyToManyField(Autor, related_name="livros")