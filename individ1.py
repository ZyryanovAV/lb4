#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    N = int(input("Введите число экзаменов -> "))
        if N <= 20:
            if N == 1:
                print(f"Мы успешно сдали {N} экзамен")
            elif 2 <= N <= 4:
                print(f"Мы успешно сдали {N} экзаменa")
            elif 5 <= N <= 20:
                print(f"Мы успешно сдали {N} экзаменов")
        else:
            print("Ошибка!")
        exit(1)
