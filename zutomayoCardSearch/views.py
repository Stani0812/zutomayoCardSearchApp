from django.shortcuts import render, redirect

# モデルとフォームを呼び出す
from .models import Search, Card
from .forms import SearchForm, CardSearchForm

# 投稿機能と投稿の表示
def search(request):
    template_name = 'search/index.html'
    contents = Search.objects.all()
    form = SearchForm(request.POST or None)
    params = {'contents': contents, 'form': form}
    if form.is_valid():
        search = form.save(commit=False)
        search.save()
        return redirect('zutomayoCardSearch:search')
    return render(request, template_name, params)

def cardSearch( request ):
    template_name_search = 'cardSearch/index.html'
    my_dict_search = {
        'form' : CardSearchForm(),
        'insert_forms': '初期値',
    }
    if ( request.method == 'POST' ):
        my_dict_search['insert_forms'] = '検索文字列:' + request.POST['searchText']
        my_dict_search['form'] = CardSearchForm( request.POST )
    return render( request, template_name_search, my_dict_search )

def cardInfo( request ):
    template_name_info = 'cardSearch/info.html'
    contents = Card.objects.values()
    header = ['画像', 'カードID', 'カード名', 'レア度', 'カードタイプ', '属性', 'クロノス', 'コスト', 'SendToPower', 'NIGHT', 'DAY', '能力タイプ', '能力']
    my_dict_info = {
        'title' : 'ずとまよカード一覧',
        'contents' : contents,
        'header' : header,
    }
    return render( request, template_name_info, my_dict_info )