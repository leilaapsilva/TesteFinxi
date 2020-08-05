#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('demandas/', views.ListaDemandas.as_view(), name='lista-demandas'),    
]