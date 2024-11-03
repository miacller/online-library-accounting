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
          print("Введите корректные данные ")

def user_operation_check():
    user_id = int(correct_check("Введите ID пользователя"))
    if user_id in users:
        confirmation = int(correct_check(f"Вы выбрали пользователя {users[user_id].name} верно? (1 - да, 0 - нет)"))
        if confirmation == 1:
            return user_id
        else:
            user_operation_check
    else:
        print("Пользователь с таким ID не найден.")
        return user_operation_check()

def book_operation_check():
    isbn = int(correct_check("Введите ISBN книги"))
    if (isbn in books) and (books[isbn].presence):
        return isbn
    elif(not(isbn in books)):
        print("Книги с таким ISBN нет в учете")
    else:
        print("Указанная книга на руках у пользователя")