from django.forms import ModelForm, fields
from .models import Pracownicy

class PracownicyForm(ModelForm):
    class Meta:
        model = Pracownicy
        fields = ['imie','nazwisko','data_ur','pesel']