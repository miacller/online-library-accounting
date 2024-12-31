# -*- coding: cp1251 -*-
import attr 
from utilits import Book, books, free_books, correct_check, book_operation_check
from users import users, User

def create_new_book():
    title = correct_check("Введите название книги: ")
    isbn = len(books) + 1
    author = correct_check("Введите фамилию автора: ")
    year = correct_check("Введите год написания книги: ")
    book = Book(title = title, author = author, year = year, isbn = isbn, presence = True)
    books[isbn] = book
    free_books[isbn] = book
    print(f"Книга {title} добвалена.\n Aвтор - {author}\n Год выпуска - {year}\n ISBN - {isbn}\n")

def delete_book():
    isbn = book_operation_check()
    choosen_book_title = books[isbn].title
    del books[isbn]
    del free_books[isbn]
    print(f"Книга {choosen_book_title} успешно удалена из учета")


def free_books_list():
    for isbn in free_books:
        print(books[isbn].title, '- ISBN:', books[isbn].isbn)

def books_user_check():
    isbn = int(correct_check("Введите ISBN книги"))
    if (isbn in books) and (not(books[isbn].presence)):
        for user_id in users:
            if isbn in users[user_id].borrowed_books:
                print('Книга на руках у пользователя с ID:', user_id)
                break
    elif(not(isbn in books)):
        print("Книги с таким ISBN нет в учете")
    else:
        print("Указанная книга свободна")
        




