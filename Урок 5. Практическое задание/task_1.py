"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections
"""
COUNT = int(input("Введите количество предприятий для расчета прибыли: "))
FIRMA = collections.namedtuple('FIRMA', ['name', 'q1', 'q2', 'q3', 'q4'])
FIRMA_1 = FIRMA(name=input("Введите название предприятия: "), q1=0, q2=0, q3=0, q4=0)
FIRMA_1.name = input("Введите название предприятия: ")

FIRMA_2 = FIRMA(name='Копыта', q1=345, q2=34, q3=543, q4=34)
print(FIRMA_1)
print(FIRMA_2)
PROFIT_FIRMA_1 = FIRMA_1.q1 + FIRMA_1.q2 + FIRMA_1.q3 + FIRMA_1.q4
PROFIT_FIRMA_2 = FIRMA_2.q1 + FIRMA_2.q2 + FIRMA_2.q3 + FIRMA_2.q4
PROFIT = (PROFIT_FIRMA_1 + PROFIT_FIRMA_2)/2
print(PROFIT_FIRMA_1)
print(PROFIT_FIRMA_2)
print(f"Средняя годовая прибыль всех предприятий: {PROFIT}")
# A = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
# print(input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split(" "))
FIRMA = collections.namedtuple('FIRMA', ['name', 'q1', 'q2', 'q3', 'q4'])
NAME_1 = input("Введите название предприятия: ")
PROFIT = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split(" ")
FIRMA_1 = FIRMA(name=NAME_1, q1=PROFIT[0], q2=PROFIT[1], q3=PROFIT[2], q4=PROFIT[3])
print(FIRMA_1)

FIRMA = collections.namedtuple('FIRMA', ['name', 'profit'])
#NAME_I = input("Введите название предприятия: ")
PROFIT_I = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split(" ")
_sum = 0
for i in PROFIT_I:
    _sum = _sum + int(i)
print(_sum)
FIRMA_1 = FIRMA(name=NAME_I, profit=PROFIT_I)
print(FIRMA_1)
print(sum(PROFIT_I))
print(f"Название фирмы: {FIRMA_1.name}")
print(f"Прибыль фирмы за год: {sum(FIRMA_1.profit)}")"""

FIRMA = collections.namedtuple('FIRMA', ['name', 'profit'])
COUNT = int(input("Введите количество предприятий для расчета прибыли: "))
PROFIT_MEAN = 0
LIST_1 = []
for i in range(1, COUNT+1):
    NAME_F = input("Введите название предприятия: ")
    PROFIT_I = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split(
        " ")
    PROFIT_Y = 0
    for j in PROFIT_I:
        PROFIT_Y = PROFIT_Y + int(j)
    LIST_1.append(FIRMA(name=NAME_F, profit=PROFIT_Y))

# print(LIST_1)

_sum = 0
for i in range(0, len(LIST_1)):
    _sum = _sum + int(LIST_1[i][1])

_sum_2 = _sum / len(LIST_1)
print(f"Средняя годовая прибыль всех предприятий: {_sum_2}")
LOW = []
HIGH = []
MEAN = []
for j in range(0, len(LIST_1)):
    if int(LIST_1[j][1]) > _sum_2:
        HIGH.append(LIST_1[j][0])
    elif int(LIST_1[j][1]) < _sum_2:
        LOW.append(LIST_1[j][0])
    else:
        MEAN.append(LIST_1[j][0])

print(f"Предприятия, с прибылью выше среднего значения: {' '.join(HIGH)}")
print(f"Предприятия, с прибылью ниже среднего значения: {' '.join(LOW)}")

print(" ".join(MEAN))
