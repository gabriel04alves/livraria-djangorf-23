from django.db import models 

class Categoria(models.Model): 
    descricao = models.CharField(max_length=100)
    
    # nome para o campo no admin
    def __str__(self): # self +- = this
        return self.descricao