from controller.manager import Library
from model.book import Book

library = Library()

while (True):
    escolha = input('1 - Cadastrar livro / 2 - listar livros: ')
    if (escolha == '1'):

        title = input("Título: ")
        author = input("Autor: ")
        year = eval(input("Ano: "))

        book = Book(title, author, year)
        library.register_book(book)

    if (escolha == '2'):
        
        library.list_books()

    print()