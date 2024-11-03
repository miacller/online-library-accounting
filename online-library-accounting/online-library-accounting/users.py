# -*- coding: cp1251 -*-
import attr 
from utilits import Book, books, free_books, User, users, correct_check,user_operation_check, book_operation_check


def create_new_user():
    name = correct_check("������� ��� ������������: ")
    user_id = len(users) + 1
    user = User(name = name, user_id = user_id)
    users[user_id] = user
    print(f"������������ {name} ��������. ��� ID - {user_id}")

def delete_user():
    user_id = int(correct_check("������� ID ������������, �������� ������ �������"))
    if (users[user_id] in users) and len(users[user_id].borrowed_books) == 0:
        name_chosed_user = users[user_id].name
        del users[user_id]
        print(f"������������ {name_chosed_user} ������� ������")
    elif(not(users[user_id] in users)):
        print("������������ � ����� ID �� ���������")
        while(user_id):
            delete_user()
    else:
        print("� ������������ ���� ����� �� �����, ����� ��������� ���������� ����� ��� �����")

def take_book():
    user_id = user_operation_check()
    isbn = book_operation_check()
    users[user_id].borrowed_books.append(books[isbn])
    books[isbn].presence = False
    del free_books[isbn]
    print(f"����� {books[isbn].title} �������� ������������ {users[user_id].name}")

def give_back_book():
    user_id = user_operation_check()
    isbn = int(correct_check("������� ISBN �����"))
    if (isbn in books) and (books[isbn] in users[user_id].borrowed_books):
        users[user_id].borrowed_books.remove(books[isbn])
        books[isbn].presence = True
        free_books[isbn] = books[isbn]
        print(f"������������ {books[isbn].title} ������ ����� {users[user_id].name}")
    elif(not(isbn in books)):
        print("����� � ����� ISBN ��� � �����")
    else:
        print("��������� ����� �� �� ����� � ������������")





