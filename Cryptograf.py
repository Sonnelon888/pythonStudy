"""В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили
каким-то странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е.
заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь
нуждаются в помощи:
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac                 """
from typing import Optional, List, Any


def crypt_gr(alphabet1, alphabet2, crypt, no_crypt):
    result = ""
    alphabet1 = list(str(ch) for ch in alphabet1)
    alphabet2 = {str(ch): str(alphabet1[alphabet2.index(ch)]) for ch in alphabet2}
    crypt = list(str(ch) for ch in crypt)
    no_crypt = list(str(ch) for ch in no_crypt)
    for ch in crypt:
        for key in alphabet2:
            if alphabet2[key] == ch:
                crypt.insert(crypt.index(alphabet2[key]), key)
                crypt.remove(ch)
                result += str(key)
    result += "\n"
    for ch in no_crypt:
        if ch in alphabet2:
            no_crypt.insert(no_crypt.index(ch), alphabet2[ch])
            no_crypt.remove(ch)
            result += str(alphabet2[ch])
    return result


print(crypt_gr(str(input()), str(input()), str(input()), str(input())))

