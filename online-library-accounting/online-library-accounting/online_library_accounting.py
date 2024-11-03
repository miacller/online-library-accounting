# -*- coding: cp1251 -*-
from random import choice
import attr
from users import create_new_user, delete_user, give_back_book, take_book
from books import create_new_book, delete_book, free_books_list
from utilits import books, users

def menu():
    text_menu = """\
    1. ���������������� ����� �����
    2. ������� ����� �� �������
    3. ���������������� ������ ������������
    4. ������� ������������ �� �������
    5. ����� �����
    6. ������� �����    
    7. ����� ������������ �����
    8. ������ ��������� ����
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
                print("������� ���������� �������� ")
        except ValueError:
            print("������� ���������� �������� ")

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
        case 8:
            free_books_list()

