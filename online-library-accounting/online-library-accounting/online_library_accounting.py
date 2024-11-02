# -*- coding: cp1251 -*-
from random import choice
import attr
from users import correct_check, create_new_user

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
        case 3:
            create_new_user()

