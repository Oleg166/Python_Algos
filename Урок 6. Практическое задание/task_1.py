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

from memory_profiler import profile
import random
import time

LIST_X = [random.randint(0, 10) for j in range(200000)]


@profile
def function_1(list_f1):
    list_1 = [list_f1.count(list_f1[i]) for i in range(0, len(list_f1))]
    return print(list_f1[list_1.index(max(list_1))])


@profile
def function_2(list_f2):
    list_2 = []
    for i in range(0, len(list_f2)):
        list_2.append(list_f2.count(list_f2[i]))
    return print(list_f2[list_2.index(max(list_2))])


@profile
def function_3(list_f3):
    numb = max(list_f3, key=list_f3.count)
    return print(numb)

if __name__ == "__main__":
    print(time.ctime())
    t1 = time.process_time()
    function_1(LIST_X)
    t2 = time.process_time()
    print('Took {} seconds'.format(t2 - t1))
    print(time.ctime())
    t3 = time.process_time()
    function_2(LIST_X)
    t4 = time.process_time()
    print('Took {} seconds'.format(t4 - t3))
    print(time.ctime())
    t5 = time.process_time()
    function_3(LIST_X)
    t6 = time.process_time()
    print('Took {} seconds'.format(t6 - t5))
    print(time.ctime())

"""
Python 3.7.5, Windows 7 x64
Результаты замеров:
Задача поиска чаще всего встречающегося элемента в списке, состоящем из 200000 эелементов.
Элементы представляют из себя цифры от 0 до 10

Замеры:
2
Line #    Mem usage    Increment   Line Contents
================================================
    23     18.6 MiB     18.6 MiB   @profile
    24                             def function_1(list_f1):
    25     26.2 MiB      0.8 MiB       list_1 = [list_f1.count(list_f1[i]) for i in range(0, len(list_f1))]
    26     26.2 MiB      0.0 MiB       return print(list_f1[list_1.index(max(list_1))])
Took 653.8469913 seconds

2
Line #    Mem usage    Increment   Line Contents
================================================
    29     18.7 MiB     18.7 MiB   @profile
    30                             def function_2(list_f2):
    31     18.7 MiB      0.0 MiB       list_2 = []
    32     27.0 MiB      0.0 MiB       for i in range(0, len(list_f2)):
    33     27.0 MiB      0.9 MiB           list_2.append(list_f2.count(list_f2[i]))
    34     27.0 MiB      0.0 MiB       return print(list_f2[list_2.index(max(list_2))])
Took 663.2070513 seconds

2
Line #    Mem usage    Increment   Line Contents
================================================
    37     19.7 MiB     19.7 MiB   @profile
    38                             def function_3(list_f3):
    39     19.7 MiB      0.0 MiB       numb = max(list_f3, key=list_f3.count)
    40     19.7 MiB      0.0 MiB       return print(numb)
Took 663.2382514999999 second

1-ая функция: с помощью генератора формируется второй список, в котором на месте каждого элемента списка указано 
сколько раз этот элемент встречается в списке. 

2-ая функция: с помощью цикла for формируется такой же второй список, как и в первой функции.

3-ая функция: наиболее часто встречающийся элемент списка находится с помощью обработки исходного списка
встроенной функцией max с параметром key.

Быстрее всех хадача рещшается с помощью первой функции. Но выигрыш по времени составляет 10 секунд, это примерно 1.5 %.
Можно сказать, что все три функции отрабатывают примерно за одно время: 660 сек.

Больше всего затрат памяти у 2-ой функции, так как для формирования второго списка программе приходится 
держать его в памяти и на каждом из 200000 добавлять в конец второго списка новый эелемент.

На втором месте по затратам памяти 1-ая функция. В ней второй список формируется с помощью генератора списка, что 
и приводит к меньшим затратам памяти.

В 3-ей функции нет инкремента в расходе памяти, так как для вычисления результата используются встроенные инструменты.
Скорее всего, инкремент есть, но он настолько мал, что не отображается для 200000 элементов. 

Таким образом, самой оптимальной для решения данной задачи является 3-ая функция, с использованием встроенных инструментов.
"""