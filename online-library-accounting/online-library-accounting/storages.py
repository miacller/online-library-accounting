# -*- coding: cp1251 -*-
import attr

@attr.s
class User:
    name: str = attr.ib()
    user_id: int = attr.ib()
    borrowed_books: list = attr.ib(factory=list)

@attr.s
class Book:
    title: str = attr.ib()
    author: str = attr.ib()
    year: int = attr.ib()
    isbn: int = attr.ib()
    presence: bool = attr.ib()

# Основные хранилища данных
users = {}
books = {}
