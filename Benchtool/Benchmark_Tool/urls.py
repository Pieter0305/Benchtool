from django.contrib import admin
from django.urls import path, include
from .views import Home, search, filedl

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', search, name='search'),
    path('download/', filedl, name='download'),

]