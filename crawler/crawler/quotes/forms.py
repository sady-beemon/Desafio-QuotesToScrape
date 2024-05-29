from django import forms
from crawler.quotes.models import Quotes

class QuotesForm(forms.ModelForm):
        class Meta:
            model = Quotes
            fields = ('content', 'creator', 'tags')