"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

n = 99
sum_1 = 0

for m in range(0, n + 1):
    sum_1 = sum_1 + m

sum_2 = n * (n + 1) / 2

print(f'Сумма    "1+2+...+n" для числа {n} равна {sum_1}.')

print(f'Выражение "n(n+1)/2" для числа {n} равно {int(sum_2)}.')