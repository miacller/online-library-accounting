# -*- coding: cp1251 -*-
import attr

@attr.s
class Book:
    title: str = attr.ib()
    author: str = attr.ib()
    year: int = attr.ib()
    isbn: int = attr.ib()
    presence: bool = attr.ib()

books = {}
free_books = {}

@attr.s
class User:
    name: str = attr.ib()
    user_id: int = attr.ib()
    borrowed_books: list = attr.ib(factory = list)

users = {}


def correct_check(value):
    while True:
      x = input(value).strip()
      if x:
          return x
      else:
          print("������� ���������� ������ ")

def user_operation_check():
    user_id = int(correct_check("������� ID ������������"))
    if user_id in users:
        confirmation = int(correct_check(f"�� ������� ������������ {users[user_id].name} �����? (1 - ��, 0 - ���)"))
        if confirmation == 1:
            return user_id
        else:
            user_operation_check
    else:
        print("������������ � ����� ID �� ������.")
        return user_operation_check()

def book_operation_check():
    isbn = int(correct_check("������� ISBN �����"))
    if (isbn in books) and (books[isbn].presence):
        return isbn
    elif(not(isbn in books)):
        print("����� � ����� ISBN ��� � �����")
    else:
        print("��������� ����� �� ����� � ������������")