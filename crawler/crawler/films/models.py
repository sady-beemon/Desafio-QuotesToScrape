from django.db import models

class Movies(models.Model):
    rank = models.IntegerField('Rank do filme',blank=True,null=True)
    title = models.TextField('Titulo do filme',blank=True, null=True)
    date = models.IntegerField('Ano do filme',blank=True,null=True)
    time = models.TextField('Tempo do filme',blank=True,null=True)
    minage = models.TextField('Idade minima',blank=True,null=True)
    score = models.TextField('Nota do filme',blank=True,null=True)