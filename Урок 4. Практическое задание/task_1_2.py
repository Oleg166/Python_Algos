"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
"""
   Голые цифры замеров и немного аналитики для задачи "переворота" числа
"""


def turn_over(i, step=87, num_2=0):
    """
    Функция переворачивает число
    """
    if step == 0:
        return # print(f"Перевернутое число: {num_2}")
    i_1 = i % 10
    i = i // 10
    num_2 = num_2 + i_1*(10**(step-1))
    step -= 1
    turn_over(i, step, num_2)


# через строку кода
STR_CODE = '''
NUMB = 129345678915234658795312465791293456789152346587953124657912934567891523465879531246579
NUMB_2 = 0
for n in range(len(str(NUMB))-1, -1, -1):
    NUMB_1 = NUMB % 10
    NUMB = NUMB // 10
    NUMB_2 = NUMB_2 + NUMB_1*(10**n)

# print(f"Перевернутое число: {NUMB_2}")
'''

N = 129345678915234658795312465791293456789152346587953124657912934567891523465879531246579

print(timeit.timeit("turn_over(N)", setup="from __main__ import turn_over, N", number=1000))
print(timeit.timeit(STR_CODE, number=1000))

"""
Для 2-х значного числа время исполнения кода примерно одинаково:
рекурсия - 0.001093
цикл     - 0.001088 

Уже с 3-х значного числа видно, что рекурсия медленнее:
рекурсия - 0.001675
цикл     - 0.001573

С увеличением разрядности числа разрыв увеличивается.
Для 87-и значного числа:
рекурсия - 0.08585
цикл     - 0.06821

Это происходит потому, что в цикле за подсчет шагов отвечает функция range, а в рекурсии шаги считаются инкрементом.
"""