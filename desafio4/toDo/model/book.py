import random

class Book:

    def __init__(self, name: str, author: str, year: int) -> None:
        self.__name = name
        self.__author = author
        self.__year = year
        self.__id = None

    def set_id(self, id: int) -> None:
        self.__id = id

    def is_valid(self) -> bool:
        if not isinstance(self.__name, str):
            return False

        if not isinstance(self.__author, str):
            return False

        if not isinstance(self.__year, int):
            return False

        return True

    def _book_not_valid_message(self) -> None:
        print("Livro inválido! ")

    def get_info(self) -> None:
        print(
            f"""
                    id: {self.__id}
                    name: {self.__name}
                    author: {self.__author}
                    year: {self.__year}
            """
            )