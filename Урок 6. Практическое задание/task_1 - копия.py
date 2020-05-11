from random import random

LIST_X = [int(random() * 10) for i in range(100)]

def function_1(list_f1):
    LIST_1 = [list_f1.count(list_f1[i]) for i in range(0, len(list_f1))]
    return print(list_f1[LIST_1.index(max(LIST_1))])

def function_2(list_f2):
    LIST_2 = []
    for i in range(0, len(list_f2)):
        LIST_2.append(list_f2.count(list_f2[i]))
    return print(list_f2[LIST_2.index(max(LIST_2))])

function_1(LIST_X)
function_2(LIST_X)
