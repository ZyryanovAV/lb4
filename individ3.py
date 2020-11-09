#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    i = 10
    while i <= 99:
        s = int((i % 10) + (i / 10))
        if i == s + s * s:
            print("Это число:", i)
        i += 1
