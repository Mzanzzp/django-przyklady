from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def listviev(request):
    return HttpResponse("lista ksiazek")