from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(),
            'content': forms.Textarea()
        }
