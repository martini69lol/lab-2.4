#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    def ten_element():
        num_list = input('Введите 10 чисел через зяпятую: ').split(',')
        num_list = list(map(int, num_list))
        result = 0
        for i in num_list:
            if 3 < i < 8:
                result += i
        print(result)


ten_element()
