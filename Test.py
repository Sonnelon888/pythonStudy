"""Выводит таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла
 и закрученной по часовой стрелке, как показано в примере n=5:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9      """
n, A = int(input()), []
A = [[i for i in range(1, n + 1)],[] ]
for i in range(n):
    for j in range(n):
        print(i, end=' ')
    print('\n', end='')