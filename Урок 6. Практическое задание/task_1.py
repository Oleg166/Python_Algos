"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""Профилировка затрат памяти"""
# https://pypi.org/project/guppy3/

"""from guppy import hpy
import copy

h = hpy()"""

"""x = list(range(100000))
y = copy.deepcopy(x)"""
"""LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = max(LIST)
print(A)
del LIST
del A"""
"""LIST_1 = [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]

MIN_INDEX = LIST_1.index(min(LIST_1))
MAX_INDEX = LIST_1.index(max(LIST_1))

if MAX_INDEX < MIN_INDEX:
    START_INDEX = MAX_INDEX+1
    END_INDEX = MIN_INDEX
else:
    START_INDEX = MIN_INDEX+1
    END_INDEX = MAX_INDEX

LIST_2 = LIST_1[START_INDEX:END_INDEX]

_SUM = 0
for i in LIST_2:
    _SUM = _SUM + i

print(f"Сумма элементов между минимальным ({min(LIST_1)}) и "
      f"максимальным ({max(LIST_1)}) элементами: {_SUM}")
print(h.heap())"""
"""
import sys

print(sys.getrefcount(1))"""


"""import copy
from memory_profiler import profile


@profile
def function_1():
    x = list(range(10000000))
    y = copy.deepcopy(x)
    return y


function_1()"""
import copy
from memory_profiler import profile
from random import random
import time

LIST_X = (int(random() * 10) for i in range(100))

@profile
def function_1(list_f1):
    LIST_1 = [list_f1.count(list_f1[i]) for i in range(0, len(list_f1))]
    return print(list_f1[LIST_1.index(max(LIST_1))])


@profile
def function_2(list_f2):
    LIST_2 = []
    for i in range(0, len(list_f2)):
        LIST_2.append(list_f2.count(list_f2[i]))
    return print(list_f2[LIST_2.index(max(LIST_2))])


@profile
def function_3():
    pass

if __name__ == "__main__":
    t1 = time.process_time()
    function_1(LIST_X)
    t2 = time.process_time()
    print('Took {} seconds'.format(t2 - t1))
    t3 = time.process_time()
    function_2(LIST_X)
    t4 = time.process_time()
    print('Took {} seconds'.format(t4 - t3))
    # function_3()
