"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recur_numb(numb, numeral, step, count_numeral = 0):
    N_1 = numb % 10
    try:
        if numeral % N_1 == 0 and numeral // N_1 == 1:
            count_numeral += 1
    except ZeroDivisionError:
        count_numeral += 1
    step -= 1
    numb = numb // 10
    if step == 0:
        return print(f"В числе {NUMBER} цифра {NUMBER_QUEST} встречается {count_numeral} раз(а).")
    recur_numb(numb, numeral, step, count_numeral)

NUMBER = int(input("Введите число: "))
NUMBER_QUEST = int(input("Введите цифру, которую надо посчитать: "))
# print(f"В числе {NUMBER} цифра {NUMBER_QUEST} встречается {recur_numb(NUMBER, NUMBER_QUEST, len(str(NUMBER)))}")
recur_numb(NUMBER, NUMBER_QUEST, len(str(NUMBER)))

COUNT = int(input("Сколько будет чисел? - "))
def recur(count, cifra, count_answer=0):
    pass