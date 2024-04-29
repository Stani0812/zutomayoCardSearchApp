from django.shortcuts import render, redirect

# モデルとフォームを呼び出す
from .models import Search
from .forms import SearchForm

# 投稿機能と投稿の表示
def search(request):
    template_name = 'search/index.html'
    contents = Search.objects.all()
    form = SearchForm(request.POST or None)
    params = {'contents': contents, 'form': form}
    if form.is_valid():
        search = form.save(commit=False)
        search.save()
        return redirect('search:search')
    return render(request, template_name, params)

