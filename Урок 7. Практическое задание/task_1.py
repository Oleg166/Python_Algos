"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random
import copy


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

def bubble_sort_modern(orig_list):
    n = 1
    orig_list_1 = []
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        if orig_list_1 == orig_list:
            break
        orig_list_1 = copy.deepcopy(orig_list)
        n += 1
    return orig_list

# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f"Исходный список из 10 элементов:\n{orig_list}")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 10 элементов:\n{bubble_sort(orig_list)}\n")

# замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f"Исходный список из 100 элементов:\n{orig_list}")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 100 элементов:\n{bubble_sort(orig_list)}\n")

# замеры 1000
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f"Исходный список из 1000 элементов:\n{orig_list}")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 1000 элементов:\n{bubble_sort(orig_list)}\n")
