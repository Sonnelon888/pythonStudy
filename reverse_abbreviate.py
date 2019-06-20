"""На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить
файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
 Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу. """


def read(file_name):
    with open(file_name + 'r')as abbrev:
        text = abbrev.readline()
        abbrev.close()
        return text


def translate(text):
    translated = ""
    for i in range(0, len(text)):
        if text[i].isalpha():
            try:
                if text[i+1].isdigit() and text[i+2].isdigit():
                    translated += text[i] * int(text[i+1]+text[i+2])
                else:
                    translated += text[i] * int(text[i + 1])
            except IndexError:
                translated += text[i] * int(text[i + 1])
        else:
            continue
    return translated


def write(text_to_file):
    with open("new_text.txt", "w")as abbrev:
        abbrev.write(text_to_file + '\n')
        abbrev.close()


write(translate(read('text.txt')))

