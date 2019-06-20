"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
"""
n = int(input())
list = [input().split(';') for x in range(n)]
vs = [(x[0], x[2]) for x in list]
import itertools
clubs = set(itertools.chain.from_iterable(vs))
res = {club:[0, 0, 0, 0, 0] for club in clubs}
for k1, gol1, k2, gol2 in list:
    res[k1][0] += 1
    res[k2][0] += 1
    if int(gol1) > int(gol2):
        res[k1][1] += 1
        res[k1][4] += 3
        res[k2][3] += 1
    elif int(gol1) < int(gol2):
        res[k2][1] += 1
        res[k2][4] += 3
        res[k1][3] += 1
    elif int(gol1) == int(gol2):
        res[k1][2] += 1
        res[k1][4] += 1
        res[k2][2] += 1
        res[k2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))
