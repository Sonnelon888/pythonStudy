"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
 удаляет из него все нечётные значения,
 а чётные нацело делит на два. Функция не должна ничего возвращать,
  требуется только изменение переданного списка"""


def modify_list(l):
    for i in reversed(range(0, len(l))):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            del l[i]


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
