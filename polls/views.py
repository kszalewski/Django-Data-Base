from polls.formularz import PracownicyForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Pracownicy, Stanowiska, Szkolenia, Urlopy, Zatrudnienie, Projekty, Premia, Rekrutacja


def detail_pracownicy(request):
    pracownicy = Pracownicy.objects.all()
    template = loader.get_template('polls/pracownicy.html')
    context = {
        'pracownicy': pracownicy,
    }
    return HttpResponse(template.render(context, request))

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

def usun_f(request,id):
    pracownik = get_object_or_404(Pracownicy, pk=id)
    if request.method == "POST":
        pracownik.delete()
        return redirect('/polls/pracownicy')
    return render(request, 'polls/usun_pracownika.html',{'id_pracownika':pracownik})

def usun_st(request,id):
    stanowisko = get_object_or_404(Stanowiska, pk=id)
    if request.method == "POST":
        stanowisko.delete()
        return redirect(detail_stanowiska)
    return render(request, 'polls/usun_stanowisko.html',{'id_stanowiska':stanowisko})

def usun_proj(request,id):
    projekt = get_object_or_404(Projekty, pk=id)
    if request.method == "POST":
        projekt.delete()
        return redirect(detail_projekty)
    return render(request, 'polls/usun_projekt.html',{'id_projektu':projekt})

def usun_zat(request,id):
    zatrudnienie = get_object_or_404(Zatrudnienie, pk=id)
    if request.method == "POST":
        zatrudnienie.delete()
        return redirect(detail_zatrudnienie)
    return render(request, 'polls/usun_zatrudnienie.html',{'id_projektu':zatrudnienie})

def form_f(request):
    formularz = PracownicyForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'polls/formularz.html', {'form':formularz})