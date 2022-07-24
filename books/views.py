from django.shortcuts import render

from books.services import book_service


# books/
def listview(request):
    print(request.GET)
    q = request.GET.get("q")
    if q:
        books = book_service.filter(q=q)
    else:
        books = book_service.get_all_books()
    return render(
        request=request,
        template_name="books/list.html",
        context={'books': books}
    )


def details(request, book_id: int):
    book = book_service.get_book(book_id)
    return render(
        request=request,
        template_name="books/details.html",
        context={'book': book}
    )