# -*- coding: cp1251 -*-
import attr 
from utilits import Book, books, free_books, correct_check, book_operation_check

def create_new_book():
    title = correct_check("������� �������� �����: ")
    isbn = len(books) + 1
    author = correct_check("������� ������� ������: ")
    year = correct_check("������� ��� ��������� �����: ")
    book = Book(title = title, author = author, year = year, isbn = isbn, presence = True)
    books[isbn] = book
    free_books[isbn] = book
    print(f"����� {title} ���������.\n A���� - {author}\n ��� ������� - {year}\n ISBN - {isbn}\n")

def delete_book():
    isbn = book_operation_check()
    choosen_book_title = books[isbn].title
    del books[isbn]
    del free_books[isbn]
    print(f"����� {choosen_book_title} ������� ������� �� �����")

def free_books_list():
    for book in free_books:
        print(f"{book.title} ID {book.isbn}")




