""""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю
оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
 физике и русскому языку по всем абитуриентам"""


def read(file_name):
    with open(file_name, 'r')as abbrev:
        text = list(l.strip() for l in abbrev)
    abbrev.close()
    return text


def write(text_to_file):
    with open("new_text.txt", "w")as new_text:
        if type(text_to_file) == list:
            for i in text_to_file:
                new_text.write(i)
        else:
            new_text.write(text_to_file)
    new_text.close()


def parser(text):
    # На вход принимается список строк значений
    data = list((i.split(",")) for i in text)
    result = list((j[0].split(";")) for j in data)
# Производится разбор массива и преобразование в массив масивов отдельных строк значений
    return result


def statistic_for_one(list_abbitur_and_value):
    result = []
    summary = list
    for i in list_abbitur_and_value:
        timed = ""
        for j in i:
            if j.isdigit():
                timed += j + " "
                summary = list(k for k in timed.split(" "))
        #print(summary)
        del summary[3]
        res = 0
        for v in range(len(summary)):
            res += int(summary[v])
        result.append(str(round((res / len(summary)), 9)) + "\n")
    return result


def statistic_all(list_abbitur_and_value):
    result = []
    print(list_abbitur_and_value)
    for j in range(1, len(list_abbitur_and_value[0])):
        print(str(j) + "j")
        res = 0
        for i in range(0, len(list_abbitur_and_value)):
            print(str(i) + "i")
            res += int(list_abbitur_and_value[i][j])
            #print(res)
        print(str(res) +"total")
        result.append(str(round((res / (len(list_abbitur_and_value))), 9)) + " ")
    print(str(result))
    return result


write(statistic_for_one(parser(read("dataset_3363_4.txt"))) + statistic_all(parser(read("dataset_3363_4.txt"))))
