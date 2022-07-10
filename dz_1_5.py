# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

print('Введите координату точки A')
ax = int(input('X: '))
ay = int(input('Y: '))
print('Введите координату точки B')
bx = int(input('X: '))
by = int(input('Y: '))
print(math.sqrt((bx-ax)**2+(by-ay)**2))           # или print(((bx-ax)**2+(by-ay)**2)**0.5)