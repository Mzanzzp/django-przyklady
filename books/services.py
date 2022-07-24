from books.utils import read_from_csv, Book


class BookService:

    @staticmethod
    def get_all_books() -> list[Book]:
        books = read_from_csv("books/data/data.csv")
        return books

    @staticmethod
    def get_book(id) -> Book:
        books = read_from_csv("books/data/data.csv")
        return books[id-1]
