# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
print('Введите координату точки, неравную нулю ')
x = int(input('X: '))
while x ==0:
    print('Вы ввели ноль, введите координату точки, неравную нулю ')
    x = int(input('X: '))
print('Введите координату точки, неравную нулю ')
y = int(input('Y: '))
while x ==0:
    print('Вы ввели ноль, введите координату точки, неравную нулю ')
    y = int(input('Y: '))
if x > 0 and y > 0:
    chet = 1
elif x < 0 and y > 0:
    chet = 2
elif x < 0 and y < 0:
    chet = 3
elif x > 0 and y < 0:
    chet = 4
print(f'Точка располагается в четверти под № {chet}')