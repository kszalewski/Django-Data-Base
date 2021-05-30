from django.contrib import admin
from django.urls import path

from . import views

app_name='polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pracownicy/', views.detail_pracownicy),
    path('stanowiska/', views.detail_stanowiska),
    path('szkolenia/', views.detail_szkolenia),
    path('urlopy/', views.detail_urlopy),
    path('zatrudnienia/', views.detail_zatrudnienie),
    path('premia/', views.detail_premia),
    path('projekty/', views.detail_projekty),
    path('rekrutacja/', views.detail_rekrutacja),
    path('usun_pracownika/<int:id>/', views.usun_f),
    path('usun_stanowisko/<int:id>/', views.usun_st),
    path('usun_projekt/<int:id>/', views.usun_proj),
    path('usun_zatrudnienie/<int:id>/', views.usun_zat),
]