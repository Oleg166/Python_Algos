"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""
a = int(input("Введите трехзначное число: "))
a1 = a % 10

aa = a // 10
a2 = aa % 10

aaa = aa // 10
a3 = aaa % 10

sum = a1 + a2 + a3
multi = a1 * a2 * a3
print(f'Сумма цифр: {sum}. \nПроизведение цифр: {multi}.')