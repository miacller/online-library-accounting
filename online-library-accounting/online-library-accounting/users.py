# -*- coding: cp1251 -*-
import attr 
from utilits import Book, books, free_books, User, users, correct_check,user_operation_check, book_operation_check


def create_new_user():
    name = correct_check("Введите имя пользователя: ")
    user_id = len(users) + 1
    user = User(name = name, user_id = user_id)
    users[user_id] = user
    print(f"Пользователь {name} добавлен. Его ID - {user_id}")

def delete_user():
    user_id = int(correct_check("Введите ID пользователя, которого хотите удалить"))
    if (users[user_id] in users) and len(users[user_id].borrowed_books) == 0:
        name_chosed_user = users[user_id].name
        del users[user_id]
        print(f"Пользователь {name_chosed_user} успешно удален")
    elif(not(users[user_id] in users)):
        print("Пользователь с таким ID не обнаружен")
        while(user_id):
            delete_user()
    else:
        print("У пользователя есть книги на руках, перед удалением необходимо сдать все книги")

def take_book():
    user_id = user_operation_check()
    isbn = book_operation_check()
    users[user_id].borrowed_books.append(books[isbn])
    books[isbn].presence = False
    del free_books[isbn]
    print(f"Книга {books[isbn].title} передана пользователю {users[user_id].name}")

def give_back_book():
    user_id = user_operation_check()
    isbn = int(correct_check("Введите ISBN книги"))
    if (isbn in books) and (books[isbn] in users[user_id].borrowed_books):
        users[user_id].borrowed_books.remove(books[isbn])
        books[isbn].presence = True
        free_books[isbn] = books[isbn]
        print(f"Пользователь {books[isbn].title} вернул книгу {users[user_id].name}")
    elif(not(isbn in books)):
        print("Книги с таким ISBN нет в учете")
    else:
        print("Указанная книга не на руках у пользователя")





