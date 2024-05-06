from django.conf import settings
from django.db import models

class Quotes(models.Model):
    content = models.TextField('Conteudo da frase',blank=True, null=True)
    creator = models.TextField('Nome do criador',blank = True,null=True)
    tags = models.TextField('Tags da Frase',blank = True,null=True)
        
    def __str__(self):
            return self.content
        
    