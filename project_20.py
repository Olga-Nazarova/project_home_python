# Определить, присутствует ли в заданном списке строк, некоторое число
import random
def check_number_in_string(string):
    strings = string.split(" ")
    strings = list(filter(None, strings))

    print(f'Задана строка "{strings}"')

    result = []
    basic = ""
    for i in strings:
        for j in i:
            if j.isnumeric():
                basic += j
        result.append(basic)
        basic = ""

    result = list(filter(None, result))
    result = [int(x) for x in result]
    if result != []:
        print(f'В строке "{string}" есть цифры {result}\n')
    else:
        print(f'В строке "{string}" нет цифр\n')


string1 = "Аппаувмы123 аива5 1234и ывмыв фыВАп"
string2 = "Аппаувмы аива и ывмыв фыВАп"

check_number_in_string(string1)
check_number_in_string(string2)