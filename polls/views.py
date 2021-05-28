from django.http import HttpResponse
from django.template import loader
from .models import Pracownicy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail_pracownicy(request):
    pracownicy = Pracownicy.objects.all()
    template = loader.get_template('polls/pracownicy.html')
    context = {
        'pracownicy': pracownicy,
    }
    return HttpResponse(template.render(context, request))

