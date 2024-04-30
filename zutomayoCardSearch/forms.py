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

class CardSearchForm( forms.Form ):
    searchText = forms.CharField( label = '検索文字入力' )
