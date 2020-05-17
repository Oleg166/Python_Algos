"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random
# COUNT = int(input("Введите количество элементов: "))

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


# orig_list = [random.uniform(0, 50) for _ in range(COUNT)]
# print(f"Исходный -        {orig_list}")
# print(f"Отсортированный - {merge_sort(orig_list)}")

# замеры 5
print("Замеры на списках из 5 элементов:")
orig_list = [random.uniform(0, 50) for _ in range(5)]
print(f"Исходный список из 5 элементов:\n{orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Отсортированный список из 5 элементов:\n{merge_sort(orig_list)}\n")
print('*'*50)

# замеры 10
print("Замеры на списках из 10 элементов:")
orig_list = [random.uniform(0, 50) for _ in range(10)]
print(f"Исходный список из 10 элементов:\n{orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Отсортированный список из 10 элементов:\n{merge_sort(orig_list)}\n")
print('*'*50)

# замеры 100
print("Замеры на списках из 100 элементов:")
orig_list = [random.uniform(0, 50) for _ in range(100)]
print(f"Исходный список из 100 элементов:\n{orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Отсортированный список из 100 элементов:\n{merge_sort(orig_list)}\n")
print('*'*50)

# замеры 1000
print("Замеры на списках из 1000 элементов:")
orig_list = [random.uniform(0, 50) for _ in range(1000)]
print(f"Исходный список из 1000 элементов:\n{orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Отсортированный список из 1000 элементов:\n{merge_sort(orig_list)}\n")
print('*'*50)

"""
Результаты замеров:
- список из 5    элементов: 0.009163
- список из 10   элементов: 0.01623
- список из 100  элементов: 0.2655
- список из 1000 элементов: 3.1706
"""