#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('demandas/', views.ListaDemandas.as_view(), name='lista-demandas'),    
    path('delete/<int:pk>/', views.DemandaDetail.as_view(), name='delete_demanda'),
]