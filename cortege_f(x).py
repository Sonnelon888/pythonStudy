"""Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое целочисленое
значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от
переданного аргумента x.
Напишите программу, которой на вход в первой строке подаётся число n — количество значений x, для которых требуется
узнать значение функции f(x), после чего сами эти n значений, каждое на отдельной строке. Программа должна после
каждого введённого значения аргумента вывести соответствующие значения функции f на отдельной строке.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода
на тесте."""


def f(x):
    return x+1


dictionary = {}
keys = []
n = int(input())
for i in range(n):
    x = int(input())
    keys.append(x)
for j in range(0, len(keys)):
    key = keys[j]
    if key in dictionary:
        print(dictionary[key])
    elif key not in dictionary:
        p = keys[j]
        dictionary[key] = f(p)
        print(dictionary.get(key))
