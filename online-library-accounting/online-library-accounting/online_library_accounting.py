# -*- coding: cp1251 -*-
from random import choice
import attr
from users import correct_check, create_new_user

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
        case 3:
            create_new_user()

