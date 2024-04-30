from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'zutomayoCardSearch'

urlpatterns = [
    path( '', views.search, name = 'search' ),
    path( 'test', views.cardSearch, name = 'cardSearch' ),
    path( 'info', views.cardInfo, name = 'cardInfo' ),
]