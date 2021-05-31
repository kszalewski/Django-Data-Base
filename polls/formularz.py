from django.forms import ModelForm, fields
from .models import Pracownicy, Premia, Projekty, Rekrutacja, Stanowiska, Szkolenia, Urlopy, Zatrudnienie

class PracownicyForm(ModelForm):
    class Meta:
        model = Pracownicy
        fields = ['imie','nazwisko','data_ur','pesel']

class PremiaForm(ModelForm):
    class Meta:
        model = Premia
        fields = ['nazwa','wiekosc','uzasadnienie','awans','data']

class ProjektForm(ModelForm):
    class Meta:
        model = Projekty
        fields = ['nazwa','od_data','do_data','koszty','profit']

class RekrutacjaForm(ModelForm):
    class Meta:
        model = Rekrutacja
        fields = ['imie','nazwisko','upload_CV','stanowisko','pesel','akceptacja']

class StanowiskaForm(ModelForm):
    class Meta:
        model = Stanowiska
        fields = ['nazwa','dzial','braki']

class SzkoleniaForm(ModelForm):
    class Meta:
        model = Szkolenia
        fields = ['nazwa','certyfikat','data','cena','dofinansowanie','pracownik']

class UrlopyForm(ModelForm):
    class Meta:
        model = Urlopy
        fields = ['od_data','do_data','pracownik','miejsce_pobytu','rodzaj_zwolnienia']

class ZatrudnieniaForm(ModelForm):
    class Meta:
        model = Zatrudnienie
        fields = ['pracownik','projekt','od_data','do_data','pensja','stanowisko']

