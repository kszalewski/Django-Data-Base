from django.http import HttpResponse
from django.template import loader
from .models import Pracownicy, Stanowiska, Premia


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