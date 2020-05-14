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


def bubble_sort(orig_list_1):
    n = 1
    while n < len(orig_list_1):
        for i in range(len(orig_list_1)-n):
            if orig_list_1[i] < orig_list_1[i+1]:
                orig_list_1[i], orig_list_1[i+1] = orig_list_1[i+1], orig_list_1[i]
        n += 1
    return orig_list_1

def bubble_sort_modern(orig_list_2):
    n = 1
    orig_list_check = []
    while n < len(orig_list_2):
        for i in range(len(orig_list_2)-n):
            if orig_list_2[i] < orig_list_2[i+1]:
                orig_list_2[i], orig_list_2[i+1] = orig_list_2[i+1], orig_list_2[i]
        if orig_list_check == orig_list_2:
            break
        orig_list_check = copy.deepcopy(orig_list_2)
        n += 1
    return orig_list_2

# замеры 10
print("Замеры на списках из 10 элементов:")
print('*'*45)
orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_list_modern = copy.deepcopy(orig_list)
# без проверки
print(f"Исходный список из 10 элементов:\n{orig_list}")
print("Без проверки: ")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 10 элементов:\n{bubble_sort(orig_list)}\n")
# с проверкой
print(f"Исходный список из 10 элементов:\n{orig_list_modern}")
print("С проверкой: ")
print(timeit.timeit("bubble_sort_modern(orig_list)", \
    setup="from __main__ import bubble_sort_modern, orig_list", number=1000))
print(f"Отсортированный список из 10 элементов:\n{bubble_sort_modern(orig_list_modern)}")
print('*'*45)

# замеры 100
print("Замеры на списках из 100 элементов:")
print('*'*45)
orig_list = [random.randint(-100, 100) for _ in range(100)]
orig_list_modern = copy.deepcopy(orig_list)
# без проверки
print(f"Исходный список из 100 элементов:\n{orig_list}")
print("Без проверки: ")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 100 элементов:\n{bubble_sort(orig_list)}\n")
# с проверкой
print(f"Исходный список из 100 элементов:\n{orig_list_modern}")
print("С проверкой: ")
print(timeit.timeit("bubble_sort_modern(orig_list)", \
    setup="from __main__ import bubble_sort_modern, orig_list", number=1000))
print(f"Отсортированный список из 100 элементов:\n{bubble_sort_modern(orig_list_modern)}")
print('*'*45)

# замеры 1000
print("Замеры на списках из 1000 элементов:")
print('*'*45)
orig_list = [random.randint(-100, 100) for _ in range(1000)]
orig_list_modern = copy.deepcopy(orig_list)
# без проверки
print(f"Исходный список из 1000 элементов:\n{orig_list}")
print("Без проверки: ")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(f"Отсортированный список из 1000 элементов:\n{bubble_sort(orig_list)}\n")
# с проверкой
print(f"Исходный список из 1000 элементов:\n{orig_list_modern}")
print("С проверкой: ")
print(timeit.timeit("bubble_sort_modern(orig_list)", \
    setup="from __main__ import bubble_sort_modern, orig_list", number=1000))
print(f"Отсортированный список из 1000 элементов:\n{bubble_sort_modern(orig_list_modern)}")
print('*'*45)

"""
Результаты замеров:
- для списка из 10 элементов время с проверкой и без проверки примерно одинаковое: 0.01 - 0.02 с

- для списка из 100 элементов уже очевидно преимущество по времени алгоритма с проверкой (более чем в 5 раз):
без проверки - 0.4032 с
с проверкой  - 0.0686 с

- для списка из 1000 элементов преимущество по времени алгоритма с проверкой ещё больше(более чем в 60 раз):
без проверки - 41.9677 с
с проверкой  - 0.6944 с
"""
