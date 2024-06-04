from django import forms
from django.utils.safestring import SafeString
from crawler.quotes.models import Quotes

class QuotesForm(forms.ModelForm):
        
        class Meta:
            model = Quotes
            fields = ('content', 'creator', 'tags')