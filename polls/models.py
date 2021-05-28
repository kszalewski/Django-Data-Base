import datetime

from django.db import models
from django.utils import timezone


class Stanowiska(models.Model):
    nazwa = models.CharField(max_length=100)
    dzial = models.CharField(max_length=100)
    braki = models.BooleanField(default=1)
    def __str__(self):
        return self.nazwa

class Pracownicy(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=200)
    data_ur = models.DateField(auto_now=False, auto_now_add=False)
    pesel = models.DecimalField(max_digits=11, decimal_places=0)
    def __str__(self):
        return '%s %s' % (self.imie, self.nazwisko)

class Projekty(models.Model):
    nazwa = models.CharField(max_length=200)
    od_data = models.DateTimeField('date published')
    do_data = models.DateField(auto_now=False, auto_now_add=False)
    koszty = models.PositiveIntegerField()
    profit = models.IntegerField(default=0)
    def __str__(self):
        return self.nazwa
    def czas_trwania(self):
        return self.do_data - self.od_data
    def czy_trwa(self):
        return self.czas_trwania >= timezone.now() - self.od_data

class Zatrudnienie(models.Model):
    pracownik = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)
    projekt = models.ForeignKey(Projekty, on_delete=models.CASCADE)
    od_data = models.DateTimeField('date published')
    do_data = models.DateField(auto_now=False, auto_now_add=False)
    pensja = models.PositiveIntegerField()
    stanowisko = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.pracownik, self.stanowisko, self.projekt)
    def czas_trwania(self):
        return self.do_data - self.od_data
    def czy_zatrudniony(self):
        return self.czas_trwania >= timezone.now() - self.od_data

class Urlopy(models.Model):
    od_data = models.DateTimeField('date published')
    do_data = models.DateField(auto_now=False, auto_now_add=False)
    pracownik = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)
    miejsce_pobytu = models.CharField(max_length=200)
    Rodzaj_Zwolnienia_Choices = [
        ('Wy', 'Wypoczynkowy'),
        ('Ok', 'Okolicznosciowy'),
        ('Op', 'Opieka_nad_dzieckiem'),
        ('Sz', 'Szkolenia'),
        ('Zd', 'Zdrowotny'),
        ('Be', 'Bezplatny'),
    ]
    rodzaj_zwolnienia = models.CharField(max_length=2, choices=Rodzaj_Zwolnienia_Choices)
    def __str__(self):
        return self.rodzaj_zwolnienia
    def czas_trwania(self):
        return self.do_data - self.od_data
    def czy_na_urlopie(self):
        return self.czas_trwania >= timezone.now() - self.od_data

class Rekrutacja(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=200)
    upload_CV = models.FileField(upload_to='uploads/%Y/%m/%d/')
    stanowisko = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)
    pesel = models.DecimalField(max_digits=11, decimal_places=0)
    akceptacja = models.BooleanField()
    def __str__(self):
        return '%s %s' % (self.stanowisko, self.pesel)

class Szkolenia(models.Model):
    nazwa = models.CharField(max_length=200)
    certyfikat = models.BooleanField()
    data = models.DateField(auto_now=False, auto_now_add=False)
    cena = models.PositiveIntegerField()
    dofinansowanie = models.PositiveIntegerField()
    pracownik = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)
    def __str__(self):
        return self.nazwa

class Premia(models.Model):
    nazwa = models.CharField(max_length=200)
    wiekosc = models.PositiveIntegerField(default=0)
    uzasadnienie = models.TextField(max_length=7000)
    awans = models.BooleanField(default=0)
    data = models.DateTimeField('date published')
    def __str__(self):
        return self.nazwa