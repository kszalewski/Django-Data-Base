from django.shortcuts import render

def f_start(request):
    return render(request, 'start.html')