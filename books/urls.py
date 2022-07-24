from django.urls import path

from .views import listviev, details

app_name = "books"
urlpatterns = [
    path("books", listviev, name="book_list"),
    path("books/<int:book_id>",details , name="details"),
]