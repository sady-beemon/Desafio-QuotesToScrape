from django.db import models

class User(models.Model):
    user = models.TextField('Nome do usuario',blank=True, null=True)
    password = models.TextField('Senha do usuario',blank=True, null=True)