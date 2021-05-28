from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pracownicy/', views.detail_pracownicy),
    path('stanowiska/', views.detail_stanowiska),
    path('szkolenia/', views.detail_szkolenia),
    path('urlopy/', views.detail_urlopy),
    path('zatrudnienia/', views.detail_zatrudnienie),
    path('premia/', views.detail_premia),
    path('projekty/', views.detail_projekty),
    path('rekrutacja/', views.detail_rekrutacja),
]