from books.utils import read_from_csv, BookObject
from abc import abstractmethod, ABC
from typing import List

from books.models import Book
from books.utils import read_from_csv, BookObject

# class BookService:
#
#     @staticmethod
#     def get_all_books() -> list[Book]:
#         books = read_from_csv("books/data/data.csv")
#         return books
#
#     @staticmethod
#     def get_book(id) -> Book:
#         books = read_from_csv("books/data/data.csv")
#         return books[id-1]


class BookProvider(ABC):
    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book(self, id):
        pass

    @abstractmethod
    def filter(self, q):
        pass

class BookCsvProvider(BookProvider):


    def get_all_books(self) -> List[BookObject]:
        books = read_from_csv("data/data.csv")
        return books


    def get_book(self, id) -> BookObject:
        books = read_from_csv("data/data.csv")
        return books[id-1]

    def filter(self, q):
        books = read_from_csv("data/data.csv")
        books = [book or book in books if book.title.startswith(q.lower())]

class ModelsBooksProvider(BookProvider):

    def get_all_books(self) -> List[Book]:
        return Book.objects.all()

    def get_book(self, id) -> Book:
        return Book.objects.get(pk=id)

    def filter(self, q):
        return self.provider.get_book(book_id)

class BookService:

    def __init__(self, provider: BookProvider):
        self.provider = provider


    def get_all_books(self) -> List[BookObject]:
        return self.provider.get_all_books()


    def get_book(self, book_id) -> BookObject:
        return self.provider.get_book(book_id)

provider = ModelsBooksProvider()
# provider = BookCsvProvider()
book_service = BookService(provider=provider)