from typing import Dict, Type
from model.book import Book

class Library:

    def __init__(self) -> None:
        self.__books = list()
        self.__current_id = 1

    def __include_book(self, book: Type[Book]) -> None:
        book.set_id(self.__current_id)
        self.__books.append(book)
        print("Livro registrado! ")

        self.__increase_current_id()

    def __increase_current_id(self) -> None:
        self.__current_id += 1

    def register_book(self, book: Type[Book]) -> None:
        if not book.is_valid():
            return book._book_not_valid_message()

        return self.__include_book(book)

    def list_books(self) -> None:
        for book in self.__books:
            book.get_info()