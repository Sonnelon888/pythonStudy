"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может
быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми."""


def read(file_name):
    with open(file_name + 'r')as abbrev:
        text = abbrev.readline()
        abbrev.close()
        return text


def write(text_to_file):
    with open("new_text.txt", "w")as abbrev:
        abbrev.write(text_to_file + '\n')
        abbrev.close()


def most_used_word(s):
    s = input().lower().split()
    count = ''
    vf = 0
    for i in range(0, len(set(s))):
        if s.count(s[i]) > vf:
            vf = s.count(s[i])
            count = s[i] + " " + str(s.count(s[i]))
    print(count)
