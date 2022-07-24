from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def homepage(request):
    return render(
        request,
        "homepage.html",
        {
            "dane": "hej"
         }
    )

def greetings(request):
    return HttpResponse("witam")