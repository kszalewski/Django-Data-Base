from django.http import HttpResponse
from django.template import loader
from .models import Pracownicy, Projekty, Stanowiska, Premia, Rekrutacja


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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