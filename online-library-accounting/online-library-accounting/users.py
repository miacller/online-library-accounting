# -*- coding: cp1251 -*-
import attr 

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



def create_new_user():
    name = correct_check("Введите имя пользователя ")
    user_id = len(users) + 1
    user = User(name = name, user_id = user_id)
    users[user_id] = user
    print(f"Пользователь {name} добавлен. Его ID - {user_id}")


