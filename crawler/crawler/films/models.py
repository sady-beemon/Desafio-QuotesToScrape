from django.db import models

class Movies(models.Model):
    rank = models.IntegerField('Rank do filme',)
    title = models.TextField('Titulo do filme',)
    date = models.IntegerField('Ano do filme',)
    time = models.TextField('Tempo do filme',)
    minage = models.TextField('Idade minima',)
    score = models.FloatField('Nota do filme',)