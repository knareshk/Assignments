from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    f_d = {'read': ""}
    return render(request, 'FIRSTAPPLICATION/one.html', context=f_d)
