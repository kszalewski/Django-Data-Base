from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from .models import Pracownicy, PracownicyForm, Stanowiska, Szkolenia, Urlopy, Zatrudnienie, Projekty, Premia, Rekrutacja


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail_pracownicy(request):
    pracownicy = Pracownicy.objects.all()
    template = loader.get_template('polls/pracownicy.html')
    formularzPracownik = PracownicyForm(request.POST or None, request.FILES or None)
    if formularzPracownik.is_valid():
        formularzPracownik.save()
    context = {
        'pracownicy': pracownicy,
        'form': formularzPracownik
    }
    return HttpResponse(template.render(context, request))

def add_pracownik(request, question_id):
    pracownik = get_object_or_404(Pracownicy, pk=question_id)
    pracownik.save()
    return redirect(detail_pracownicy)

def detail_stanowiska(request):
    stanowiska = Stanowiska.objects.all()
    template = loader.get_template('polls/stanowiska.html')
    context = {
        'stanowiska': stanowiska,
    }
    return HttpResponse(template.render(context, request))

def detail_szkolenia(request):
    szkolenia = Szkolenia.objects.all()
    template = loader.get_template('polls/szkolenia.html')
    context = {
        'szkolenia': szkolenia,
    }
    return HttpResponse(template.render(context, request))

def detail_urlopy(request):
    urlopy = Urlopy.objects.all()
    template = loader.get_template('polls/urlopy.html')
    context = {
        'urlopy': urlopy,
    }
    return HttpResponse(template.render(context, request))

def detail_zatrudnienie(request):
    zatrudnienia = Zatrudnienie.objects.all()
    template = loader.get_template('polls/zatrudnienia.html')
    context = {
        'zatrudnienia': zatrudnienia,
    }
    return HttpResponse(template.render(context, request))

def detail_premia(request):
    premia = Premia.objects.all()
    template = loader.get_template('polls/premia.html')
    context = {
        'premia': premia,
    }
    return HttpResponse(template.render(context, request))

def detail_projekty(request):
    projekty = Projekty.objects.all()
    template = loader.get_template('polls/projekty.html')
    context = {
        'projekty': projekty,
    }
    return HttpResponse(template.render(context, request))

def detail_rekrutacja(request):
    rekrutacja = Rekrutacja.objects.all()
    template = loader.get_template('polls/rekrutacja.html')
    context = {
        'rekrutacja': rekrutacja,
    }
    return HttpResponse(template.render(context, request))