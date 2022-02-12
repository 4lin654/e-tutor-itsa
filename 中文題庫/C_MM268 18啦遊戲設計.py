# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 01:32:55 2022

@author: small
"""

while True:
    array = []
    total = 0

    number = int(input())
    array.append(number)

    number1 = int(input())
    array.append(number1)

    number2 = int(input())
    array.append(number2)

    number3 = int(input())
    array.append(number3)

    array.sort()

    if array[0] == array[1] == array[2] == array[3]:
        print('WIN')
    elif (array[0] != array[1] != array[2] != array[3]):
        print('R')
    elif (array[0] == array[1] == array[2]) or (array[1] == array[2] == array[3]):
        print('R')
    elif (array[0] == array[1]) or (array[2] == array[3]):
        total += (int(array[2]) + int(array[3]))
        print('%d'%total)