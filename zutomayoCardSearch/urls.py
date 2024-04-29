from django.contrib import admin
from django.urls import path, include
# views.pyからsearchを呼び出す
from .views import search

app_name = 'zutomayoCardSearch'

urlpatterns = [
    path('', search, name='search'),
]