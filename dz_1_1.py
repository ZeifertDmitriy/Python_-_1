# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num_day = int(input('Введите цифру дня недели: '))
if num_day > 7 or num_day < 1:
    print('Введена некорректная циифра')
elif num_day >= 6:
    print('Выходной')
elif num_day < 6:
    print('Будний')