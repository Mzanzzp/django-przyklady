from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from books.services import BookService
from books.utils import read_from_csv


def listviev(request):
    books = BookService.get_all_books()
    # books = read_from_csv("books/data/data.csv")
    return render(
        request,
        "books.html",
        context = {'books': books},

    )

def details(request, book_id: int):
    # books = read_from_csv("books/data/data.csv")
    # book = books[book_id-1]
    book = BookService.get_book(book_id)
    return render(
        request=request,
        template_name="details.html",
        context={'book': book}
    )