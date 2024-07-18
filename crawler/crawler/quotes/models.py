from django.conf import settings
from django.db import models

class Quotes(models.Model):
    content = models.TextField('Conteudo da frase',blank=False, null=False)
    creator = models.TextField('Nome do criador',blank = False,null=False)
    tags = models.TextField('Tags da Frase',blank = False,null=False)
        
    def __str__(self):
            return self.content
        
    