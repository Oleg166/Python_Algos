"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
try:
    NUM_1 = int(input("Введите первое число: "))
    NUM_2 = int(input("Введите второе число: "))
    NUM_3 = int(input("Введите третье число: "))

    if NUM_1 > NUM_2:
        NUM_MAX = NUM_1
        NUM_MIN = NUM_2
    else:
        NUM_MAX = NUM_2
        NUM_MIN = NUM_1

    if NUM_MAX < NUM_3:
        NUM_MAX = NUM_3

    if NUM_MIN > NUM_3:
        NUM_MIN = NUM_3

    NUM_MEAN = NUM_1 + NUM_2 + NUM_3 - NUM_MAX - NUM_MIN

    print(f"Среднее число: {NUM_MEAN}")

except ValueError:
    print("Вы ввели нечисло. Попробуйте заново")
