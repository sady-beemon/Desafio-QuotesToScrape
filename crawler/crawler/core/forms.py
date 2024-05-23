from django import forms
from crawler.core.models import User

class PostForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('user', 'password',)