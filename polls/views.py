from polls.formularz import PracownicyForm, PremiaForm, ProjektForm, RekrutacjaForm, StanowiskaForm, SzkoleniaForm, UrlopyForm, ZatrudnieniaForm
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
        return redirect('/polls/stanowiska')
    return render(request, 'polls/usun_stanowisko.html',{'id_stanowiska':stanowisko})

def usun_proj(request,id):
    projekt = get_object_or_404(Projekty, pk=id)
    if request.method == "POST":
        projekt.delete()
        return redirect('/polls/projekty')
    return render(request, 'polls/usun_projekt.html',{'id_projektu':projekt})

def usun_zat(request,id):
    zatrudnienie = get_object_or_404(Zatrudnienie, pk=id)
    if request.method == "POST":
        zatrudnienie.delete()
        return redirect('/polls/zatrudnienia')
    return render(request, 'polls/usun_zatrudnienie.html',{'id_projektu':zatrudnienie})

def form_f(request):
    formularz = PracownicyForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/pracownicy')
    return render(request, 'polls/formularz.html', {'form':formularz})

def form_prem(request):
    formularz = PremiaForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/premia')
    return render(request, 'polls/formularz_premia.html', {'form_premia':formularz})

def form_proj(request):
    formularz = ProjektForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/projekty')
    return render(request, 'polls/formularz_projekty.html', {'form_projekty':formularz})

def form_rekr(request):
    formularz = RekrutacjaForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/rekrutacja')
    return render(request, 'polls/formularz_rekrutacja.html', {'form_rekrutacja':formularz})

def form_stan(request):
    formularz = StanowiskaForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/stanowiska')
    return render(request, 'polls/formularz_stanowiska.html', {'form_stanowiska':formularz})

def form_szkol(request):
    formularz = SzkoleniaForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/szkolenia')
    return render(request, 'polls/formularz_szkolenia.html', {'form_szkolenia':formularz})

def form_urlop(request):
    formularz = UrlopyForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/urlopy')
    return render(request, 'polls/formularz_urlopy.html', {'form_urlopy':formularz})

def form_zatr(request):
    formularz = ZatrudnieniaForm(request.POST or None, request.FILES or None)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/zatrudnienia')
    return render(request, 'polls/formularz_zatrudnienia.html', {'form_zatrudnienia':formularz})

def edycja_s(request,id):
    stan = get_object_or_404(Stanowiska, pk=id)
    formularz = StanowiskaForm(request.POST or None, request.FILES or None, instance=stan)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/stanowiska')
    return render(request, 'polls/formularz_stanowiska.html', {'form_stanowiska':formularz})

def edycja_proj(request,id):
    stan = get_object_or_404(Projekty, pk=id)
    formularz = ProjektForm(request.POST or None, request.FILES or None, instance=stan)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/projekty')
    return render(request, 'polls/formularz_projekty.html', {'form_projekty':formularz})

def edycja_zatr(request,id):
    stan = get_object_or_404(Zatrudnienie, pk=id)
    formularz = ZatrudnieniaForm(request.POST or None, request.FILES or None, instance=stan)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/zatrudnienia')
    return render(request, 'polls/formularz_zatrudnienia.html', {'form_zatrudnienia':formularz})

def edycja_rekr(request,id):
    stan = get_object_or_404(Rekrutacja, pk=id)
    formularz = RekrutacjaForm(request.POST or None, request.FILES or None, instance=stan)
    if formularz.is_valid():
        formularz.save()
        return redirect('/polls/rekrutacja')
    return render(request, 'polls/formularz_rekrutacja.html', {'form_rekrutacja':formularz})