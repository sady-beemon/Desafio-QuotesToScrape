from django import forms
from crawler.films.models import Movies

class MovieForm(forms.ModelForm):
        class Meta:
            model = Movies
            fields = ('rank', 'title', 'date', 'time', 'minage', 'score',)