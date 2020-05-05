"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
import collections

FIRMA = collections.namedtuple('FIRMA', ['name', 'profit'])
LIST_1 = [FIRMA(name='A', profit=4), FIRMA(name='B', profit=8), FIRMA(name='C', profit=14)]


_sum = 0
for i in range(0, len(LIST_1)):
    _sum = _sum + int(LIST_1[i][1])

_sum_2 = _sum / len(LIST_1)
print(_sum_2)
LOW = []
HIGH = []
MEAN = []
for j in range(0, len(LIST_1)):
    if int(LIST_1[j][1]) > _sum_2:
        LOW.append(LIST_1[j][0])
    elif int(LIST_1[j][1]) < _sum_2:
        HIGH.append(LIST_1[j][0])
    else:
        MEAN.append(LIST_1[j][0])

print(" ".join(LOW))
print(" ".join(HIGH))
print(" ".join(MEAN))
