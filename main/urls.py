from django.urls import path

from .views import homepage, greetings


urlpatterns = [
    path("", homepage),
    path("greetings", greetings),
]