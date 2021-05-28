from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pracownicy/', views.detail_pracownicy),
    path('stanowiska/', views.detail_stanowiska),
    path('premia/', views.detail_premia),
    path('projekty/', views.detail_projekty),
    path('rekrutacja/', views.detail_rekrutacja),
]