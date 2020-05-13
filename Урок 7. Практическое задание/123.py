"""LIST_1 = [1, 3, 3, 4, 5, 7, 8, 9]
LIST_2 = [1, 2, 3, 4, 5, 7, 8, 9]
A = None
Q = 1
S = 0
while Q != 0:
    if LIST_1[S] != LIST_2[S]:
        print("Списки не идентичны")
        break
    elif S == len(LIST_1)-1:
        print("Списки идентичны")
        break
    else:
        S += 1


if LIST_1 == LIST_2:
    print("A")
else:
    print("B")"""
import random
import copy

def bubble_sort(orig_list):
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


# orig_list = [random.randint(0, 10) for _ in range(4)]
orig_list = [8, 9, 5, 4, 3, 2, 1]
print(bubble_sort(orig_list))
