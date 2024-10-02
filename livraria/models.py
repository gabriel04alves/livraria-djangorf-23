from django.db import models

# Create your models here.
class Categoria(models.Model): 
    descricao = models.CharField(max_length=100)
    
    # nome para o campo no admin
    def __str__(self): # self +- = this
        return self.descricao
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
                            #nulo,    #pode ser em branco
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    # alterar o nome da classe
    class Meta:
        # nome do modelo no singular
        verbose_name = "Autor"
        # alterar o nome da classe no plural (o padrão é acrescentar um 's')
        verbose_name_plural = "Autores"

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

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
    
    autores = models.ManyToManyField(Autor, related_name="livros")