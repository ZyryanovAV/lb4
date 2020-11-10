#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a_1, b_1, c_1 = map(int, input("Введите коэффициенты первой прямой (через пробел) -> ").split())
    a_2, b_2, c_2 = map(int, input("Введите коэффициенты второй прямой (через пробел) -> ").split())
    k = 0
    if a_1 == 0 and b_1 == 0:
        k += 1
    if a_2 == 0 and b_2 == 0:
        k += 1
    if k == 1:
        print("Одна из прямых не существует")
    elif k == 2:
        print("Обе прямые не существуют")
    elif a_1 == a_2 and b_1 == b_2 and c_1 == c_2:
        print("Прямые совпадают")
    elif a_1 * b_2 - b_1 * a_2 == 0:
        print("Прямые параллельны")
    else:
        x = (b_1 * c_2 - b_2 * c_1) / (a_1 * b_2 - b_1 * a_2)
        y = (a_2 * c_1 - a_2 * c_2) / (a_1 * b_2 - b_1 * a_2)
        print("Координаты точки пересечения: ")
        print("x = ", x, "y = ", y)
