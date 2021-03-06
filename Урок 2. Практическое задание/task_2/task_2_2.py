"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

NUMB = int(input("Введите число: "))


def recur(n_1, even=0, odd=0):
    """
    Программа подсчета четных и нечетных цифр в числе
    """
    el_1 = n_1 % 10
    if el_1 % 2 == 0:
        even += 1
    else:
        odd += 1
    n_1 = n_1 // 10
    if n_1 == 0:
        return print(f"Количество цифр в числе {even+odd}. Четные: {even}. Нечетные {odd}.")
    recur(n_1, even, odd)


print(f"Число {NUMB}.")
recur(NUMB)
