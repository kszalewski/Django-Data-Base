from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail_stanowiska(request, Stanowiska.nazwa):
    return HttpResponse("Ogladasz stanowisko %s." % Stanowiska.nazwa)

def results_stanowiska(request, Stanowiska.nazwa):
    response = "Szczególy stanowiska o nazwie %s."
    return HttpResponse(response % Stanowiska.nazwa)

def vote_stanowiska(request, Stanowiska.nazwa):
    return HttpResponse("Zmieniles stanowisko o nazwie %s." % Stanowiska.nazwa)