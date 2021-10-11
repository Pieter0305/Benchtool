from django.contrib import admin
from django.urls import path, include
from .views import Home, About, search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('search/', search, name='search'),

]