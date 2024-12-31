# -*- coding: cp1251 -*-
from random import choice
import attr
from users import create_new_user, delete_user, give_back_book, take_book
from books import create_new_book, delete_book, free_books_list, books_user_check
from utilits import books, users, free_books

def menu():
    text_menu = """\
    1. Зарегистрировать новую книгу
    2. Удалить книгу из реестра
    3. Зарегистрировать нового пользователя
    4. Удалить пользователя из реестра
    5. Взять книгу
    6. Вернуть книгу    
    7. Найти пользователя книги
    8. Список доступных книг
    """
    return text_menu

def print_free_books():
    print(free_books)

while(True):
    print(menu())
    while True:
        try:
            choice = int(input())
            if (1 <= choice <= 8):
                break
            else:
                print("Введите корректное значение ")
        except ValueError:
            print("Введите корректное значение ")

    match choice:
        case 1:
            create_new_book()
        case 2:
            delete_book()
        case 3:
            create_new_user()
        case 4:
            delete_user()
        case 5:
            take_book()
        case 6:
            give_back_book()
        case 7:
            books_user_check()
        case 8:
            free_books_list()

