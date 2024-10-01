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
        return self.name