from django.urls import path

from .views import listviev


urlpatterns = [
    path("posts", listviev),
]